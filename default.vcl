vcl 4.0;

backend default {
  .host = "172.21.0.4:80";
}

backend default_throttle {
  .host = "172.21.0.4:80";
  .max_connections = 1;
}

sub vcl_recv {
    if (req.url ~ "delay") {
        set req.backend_hint = default_throttle;
    } else {
        set req.backend_hint = default;
    }
}
