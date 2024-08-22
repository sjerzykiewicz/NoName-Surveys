package main

import (
	"context"
	"errors"
	"log"
	"net/http"
	"os/signal"
	"syscall"

	"github.com/sjerzykiewicz/NoName-Surveys/backend-go/internal/config"
	"github.com/sjerzykiewicz/NoName-Surveys/backend-go/internal/server"
)

func main() {
	ctx, stop := signal.NotifyContext(context.Background(), syscall.SIGINT, syscall.SIGTERM)
	defer stop()

	config, err := config.LoadConfig("dev")
	if err != nil {
		log.Fatal(err)
	}

	log.Println(config)

	server, err := server.Create(config.ServerPort)
	if err != nil {
		log.Fatal(err)
	}

	go func() {
		if err := server.ListenAndServe(); err != nil && !errors.Is(err, http.ErrServerClosed) {
			log.Fatalf("listen and serve returned an err: %v", err)
		}
	}()

	<-ctx.Done()
	log.Println("got interruption signal")
	if err := server.Shutdown(context.TODO()); err != nil {
		log.Printf("server shutdown returned an err: %v", err)
	}

	log.Println("server gracefully stopped")
}
