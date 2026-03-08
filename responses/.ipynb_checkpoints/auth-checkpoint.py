import base64
import json
from azure.identity import (
    DefaultAzureCredential,
    AzureCliCredential,
    DeviceCodeCredential
)

def acquire_bearer_token(
    scope: str = "https://ai.azure.com/.default",
    auth_method: str | None = None
) -> tuple[str, dict]:
    """
    Acquire a Microsoft Entra ID token for Azure OpenAI / Foundry endpoints.
    Supports forced authentication method selection and extracts user identity
    directly from the JWT token claims.
    
    Parameters:
        scope (str): Token scope (default: Foundry).
        auth_method (str | None): Force a specific credential type.
            Allowed values: "default", "cli", "device".
            If None, fallback chain is used.
    
    Returns:
        (token, user_info) where:
            token (str): The acquired bearer token.
            user_info (dict): Identity information extracted from JWT claims.
    """

    # Select credential based on forced method
    if auth_method == "default":
        cred = DefaultAzureCredential(exclude_powershell_credential=True)
    elif auth_method == "cli":
        cred = AzureCliCredential()
    elif auth_method == "device":
        cred = DeviceCodeCredential()
    else:
        # Automatic fallback chain
        try:
            cred = DefaultAzureCredential(exclude_powershell_credential=True)
            token = cred.get_token(scope)
        except Exception:
            try:
                cred = AzureCliCredential()
                token = cred.get_token(scope)
            except Exception:
                cred = DeviceCodeCredential()
                token = cred.get_token(scope)
        else:
            user_info = _decode_jwt_claims(token.token)
            return token.token, user_info

    # If a forced method was selected, or fallback selected a credential:
    token = cred.get_token(scope)
    user_info = _decode_jwt_claims(token.token)
    return token.token, user_info


def _decode_jwt_claims(access_token: str) -> dict:
    """
    Decode the JWT access token and extract user identity claims.
    This avoids calling Microsoft Graph, which would require a different audience.
    """
    try:
        # JWT format: header.payload.signature
        parts = access_token.split(".")
        if len(parts) < 2:
            return {"error": "Invalid JWT format"}

        payload = parts[1]
        # Add padding if needed
        payload += "=" * (-len(payload) % 4)
        decoded = base64.urlsafe_b64decode(payload)
        claims = json.loads(decoded)

        # Extract useful identity fields
        return {
            "name": claims.get("name"),
            "preferred_username": claims.get("preferred_username"),
            "oid": claims.get("oid"),
            "tid": claims.get("tid"),
            "upn": claims.get("upn"),
            "raw_claims": claims
        }
    except Exception as e:
        return {"error": f"Failed to decode JWT: {e}"}