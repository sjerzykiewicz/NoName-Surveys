package server

import (
	"net/http"

	"github.com/sjerzykiewicz/NoName-Surveys/backend-go/internal/handlers"
)

func Create(port string) (*http.Server, error) {
	server := &http.Server{}
	server.Addr = port

	sm := http.NewServeMux()
	sm.HandleFunc("/ping", handlers.PingPong)

	server.Handler = sm

	return server, nil
}
