package config

import (
	"fmt"

	"github.com/spf13/viper"
)

type Config struct {
	DbHost     string
	DbPort     string
	DbUser     string
	DbPassword string
	DbName     string
	ServerPort string
}

func LoadConfig(appMode string) (Config, error) {
	config := Config{}

	viper.SetConfigName("config")
	viper.AddConfigPath("./")

	err := viper.ReadInConfig()
	if err != nil {
		return config, fmt.Errorf("fatal error config file: %v", err)
	}

	err = viper.UnmarshalKey(appMode, &config)
	if err != nil {
		return config, fmt.Errorf("unable to decode maMode into struct, %v", err)
	}

	return config, nil
}
