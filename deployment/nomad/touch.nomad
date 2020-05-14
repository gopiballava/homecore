job "batch_touch" {

datacenters = ["bv1"]

type = "batch"

group "cache" {
    count = 1

    restart {
        attempts = 2
        interval = "30m"

        delay = "12s"

        mode = "fail"
    }

    ephemeral_disk {
        size = 300
    }

       task "script"{
       driver = "raw_exec"
      meta {
        my-key = "${TEST_VAR}"
      }
   
       config {
       command = "/usr/bin/touch"
       args = ["/tmp/success"]
            }
        }
}
}
