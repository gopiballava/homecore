# Increase log verbosity
log_level = "DEBUG"

# Setup data dir
data_dir = "/tmp/server1"

server {
  enabled          = true
  bootstrap_expect = 3

  # This is the IP address of the first server provisioned
  server_join {
    retry_join = ["192.168.88.16:4648"]
  }
}

