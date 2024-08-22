package handlers

import (
	"fmt"
	"net/http"
)

func PingPong(w http.ResponseWriter, _ *http.Request) {
	fmt.Fprintf(w, "Pong!")
}
