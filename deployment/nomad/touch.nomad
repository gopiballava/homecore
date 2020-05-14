job "batch_touch" {

datacenters = ["bv1"]

type = "service"

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
       command = "/home/automation/homecore/deployment/nomad/touchloop.sh"
       args = []
            }
        }
}
}
