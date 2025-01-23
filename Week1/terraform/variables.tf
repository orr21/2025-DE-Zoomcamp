variable "credentials" {
  description = "My Credentials"
  default     = "~/.gcloud/credentials.json"
}

variable "project" {
  description = "Project"
  default     = "dtc-de-course-447617"
  type = string
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "DE_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}