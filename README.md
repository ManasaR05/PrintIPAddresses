# IP Address Extractor (ip_print)

This project provides a Python script ip_print.py and associated tests test.robot to extract IP addresses from structured JSON file. It's designed to be integrated into a Jenkins pipeline for automation.

## Purpose

The ip_print.py script is used to extract IP addresses from JSON files with specific structures. It can handle two types of input:

1.*Files with only "vm_private_ips":* Extracts IP addresses from within the nested value dictionary under vm_private_ips.

2.*Files with both "vm_private_ips" and "network":* Extracts both private IPs and their corresponding network IPs (if available).

## Features

•*Robust Error Handling:* Checks for file existence, valid JSON format, and required data structure providing informative error messages.

•*Input:* Accepts JSON files with or without the network section.

•*Jenkins Integration:* Includes a Jenkinsfile for easy integration into a Jenkins pipeline.

•*Automated Testing:* Uses Robot Framework to validate script functionality and error handling.

