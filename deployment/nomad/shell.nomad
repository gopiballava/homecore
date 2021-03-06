job "example" {

datacenters = ["bv1"]

type = "service"

update {
    max_parallel = 1

    min_healthy_time = "10s"

    healthy_deadline = "3m"

    progress_deadline = "10m"

    auto_revert = false

    canary = 0
}
migrate {

    max_parallel = 1

    health_check = "checks"

    min_healthy_time = "10s"

    healthy_deadline = "5m"
}

group "cache" {
    count = 1

    restart {
        attempts = 2
        interval = "30m"

        delay = "15s"

        mode = "fail"
    }

    ephemeral_disk {
        size = 300
    }

       task "script"{
       driver = "raw_exec"
   
       config {
       command = "/usr/bin/touch"
       args = ["/tmp/success"]
            }
        }
}
}
