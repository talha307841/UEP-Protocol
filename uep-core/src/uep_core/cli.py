import argparse
import logging
from uep_core.client import UEPClient
from uep_core.config import load_config

def main():
    parser = argparse.ArgumentParser(description="Universal Exchange Protocol (UEP) CLI")
    parser.add_argument('--send', type=str, help='Send a message to the UEP system')
    parser.add_argument('--model', type=str, help='Specify the model to interact with')
    parser.add_argument('--list-models', action='store_true', help='List all registered models')
    
    args = parser.parse_args()
    
    config = load_config()
    client = UEPClient(config)

    if args.send:
        response = client.send_message(args.model, args.send)
        logging.info(f"Response: {response}")
    
    if args.list_models:
        models = client.list_models()
        logging.info("Registered models:")
        for model in models:
            logging.info(f"- {model}")

if __name__ == "__main__":
    main()