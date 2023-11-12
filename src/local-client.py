#!/usr/bin/env python3
"""
set up ssh tunnel between client and remote



"""
import subprocess



def set_up_ssh_tunnel(remote_machine: str, remote_user: str):
    """
        Set up the ssh tunnel

        TODO:
            use ssh to setup the tunnel
            ssh -R -N port:localhost:port remote_user@remote_host
        TODO:
            return the local addr of the tunnel
    """
