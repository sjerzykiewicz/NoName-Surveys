package config

import (
	"fmt"

	"github.com/spf13/viper"
)

type Config struct {
	DBHost     string
	DBPort     string
	DBUser     string
	DBPassword string
	DBName     string
	ServerPort string
}

func LoadConfig(appMode string) (Config, error) {
	var config Config

	viper.SetConfigName("config")
	viper.AddConfigPath("./")

	err := viper.ReadInConfig()
	if err != nil {
		return config, fmt.Errorf("fatal error config file: %w", err)
	}

	err = viper.UnmarshalKey(appMode, &config)
	if err != nil {
		return config, fmt.Errorf("unable to decode maMode into struct, %w", err)
	}

	return config, nil
}
