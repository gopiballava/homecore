# Increase log verbosity
log_level = "DEBUG"

# Setup data dir
data_dir = "/tmp/server2"

server {
  enabled          = true
  bootstrap_expect = 1

  # This is the IP address of the first server provisioned
  server_join {
    retry_join = [
      "127.0.0.1:4648",
      "192.168.88.16:4648",
    ]
  }
}

