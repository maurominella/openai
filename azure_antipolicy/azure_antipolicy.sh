#!/bin/bash

echo "Starting conditional update at $(date)"

### Check First Storage Account
first_storage=$(az graph query -q "resources | where type =~ 'microsoft.storage/storageaccounts' | project name, location, resourceGroup" --query "data[0]")

first_name=$(echo "$first_storage" | jq -r '.name')
first_rg=$(echo "$first_storage" | jq -r '.resourceGroup')

shared_key_access=$(az storage account show --name "$first_name" --resource-group "$first_rg" --query "allowSharedKeyAccess" -o tsv)
echo "The shared key access of the storage account $first_name is $shared_key_access"

### Check First CosmosDB Account
first_cosmos=$(az graph query -q "resources | where type =~ 'microsoft.documentdb/databaseaccounts' | project name, location, resourceGroup" --query "data[0]")

cosmos_exists=$(echo "$first_cosmos" | jq -r '.name')

if [ "$cosmos_exists" != "null" ]; then
  cosmos_name=$(echo "$first_cosmos" | jq -r '.name')
  cosmos_rg=$(echo "$first_cosmos" | jq -r '.resourceGroup')

  public_access=$(az cosmosdb show --name "$cosmos_name" --resource-group "$cosmos_rg" --query "publicNetworkAccess" -o tsv)
else
  public_access="Enabled"  # Default to enabled if no CosmosDB exists
fi

echo "The public access of the cosmosdb account $first_cosmos is $public_access"

### Conditional Execution
if [ "$shared_key_access" == "false" ] || [ "$public_access" == "Disabled" ]; then
  echo "Update required. Proceeding with storage and CosmosDB updates..."
  # Get storage account info using Azure Resource Graph
  storage_accounts=$(az graph query -q "resources | where type =~ 'microsoft.storage/storageaccounts' | project name, location, resourceGroup" --query "data")

  # Loop through each storage account and update settings
  echo "$storage_accounts" | jq -c '.[]' | while read -r storage_account; do
    name=$(echo "$storage_account" | jq -r '.name')
    rg=$(echo "$storage_account" | jq -r '.resourceGroup')
    echo "Updating $name in resource group $rg"
    az storage account update \
      --name "$name" \
      --resource-group "$rg" \
      --allow-shared-key-access true \
      --public-network-access Enabled
  done


  echo "Starting CosmosDB account update at $(date) (this may take 15 minutes or more...)"
  cosmosdb_accounts=$(az graph query -q "resources | where type =~ 'microsoft.documentdb/databaseaccounts' | project name, location, resourceGroup" --query "data")
  # Loop through each cosmosdb account and update settings
  echo "$cosmosdb_accounts" | jq -c '.[]' | while read -r cosmosdb_account; do
    name=$(echo "$cosmosdb_account" | jq -r '.name')
    rg=$(echo "$cosmosdb_account" | jq -r '.resourceGroup')
    echo "Updating $name in resource group $rg"
    az cosmosdb update \
      --name "$name" \
      --resource-group "$rg" \
      --public-network-access Enabled
  done

  echo "Update process completed at $(date)"

else
  echo "Shared key access is already enabled for $first_name. Skipping update."
fi