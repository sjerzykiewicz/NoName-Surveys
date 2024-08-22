package handlers

import (
	"fmt"
	"net/http"
)

func PingPong(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Pong!")
}
