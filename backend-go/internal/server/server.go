package server

import (
	"net/http"
	"time"

	"github.com/sjerzykiewicz/NoName-Surveys/backend-go/internal/handlers"
)

func Create(port string) (*http.Server, error) {
	sm := http.NewServeMux()
	sm.HandleFunc("/ping", handlers.PingPong)

	//nolint: gomnd // 10 seconds now hardcoded
	server := &http.Server{
		Addr:              port,
		Handler:           sm,
		ReadTimeout:       10 * time.Second,
		ReadHeaderTimeout: 0,
	}

	return server, nil
}
