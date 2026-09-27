# Terraform HCL to configure Vault Database Dynamic Secrets Engine

resource "vault_database_secrets_mount" "db" {
  path        = "database"
  description = "Dynamic credentials generation for production database"
}

resource "vault_database_secret_backend_connection" "postgres" {
  backend       = vault_database_secrets_mount.db.path
  name          = "postgres"
  allowed_roles = ["readonly", "readwrite"]

  postgresql {
    connection_url = "postgresql://{{username}}:{{password}}@db.production.local:5432/app"
  }
}

resource "vault_database_secret_backend_role" "readonly" {
  backend             = vault_database_secrets_mount.db.path
  name                = "readonly"
  db_name             = vault_database_secret_backend_connection.postgres.name
  creation_statements = ["CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";"]
  default_ttl         = 3600
  max_ttl             = 86400
}
