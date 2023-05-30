#!/usr/bin/env python3
"""
CHANGE_ME
"""
import argparse

def main():
    """
    entry point
    """
    parser = argparse.ArgumentParser(description='do something')
    parser.add_argument('--demo', action='store_true', help='Generate Demo Msg')
    args = parser.parse_args()

    if args.demo:
        print("Demo")

if __name__ == "__main__":
    main()
