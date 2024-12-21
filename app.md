**Connecting to LAMMA 3.1 Remotely**
=====================================

You can run LAMMA 3.1 on one machine and access it remotely from another 
host.

### Option 1: SSH Tunneling
-----------------------------

* On your local machine, run LAMMA 3.1 using `mpirun` or `mpiexec` with 
the `-np <num_nodes>` option.
* From the remote host, create an SSH tunnel using a tool like `sshuttle`, 
`autossh`, or `ssh -L`.
```bash
Remote Host:
ssh -L 8080:localhost:8080 username@remote-host-ip

Local Machine:
mpirun -np 4 ./lammasim.x <input_file>
```
### Option 2: LAMMA 3.1's Built-in MPI Library
---------------------------------------------

* Configure the integrated MPI implementation to connect to a remote host 
using `mpich` or `openmpi`.
```bash
# Example configuration file for mpich
mpich_config:
  hostname: remote-host-ip
  port: 8080
```
### Option 3: SLURM (Simple Linux Utility for Resource Management)
----------------------------------------------------------------

* Create a `slurm.conf` file on the remote host to define the nodes and 
their configuration.
* On your local machine, create a job script that uses the SLURM API to 
connect to the remote host and execute the LAMMA simulation.

Example Job Script:
```bash
#!/bin/bash

#SBATCH -J my_job
#SBATCH -n 4
#SBATCH --nodes=2

ssh username@remote-host-ip "mpirun -np 4 ./lammasim.x <input_file>"
```
### Option 4: Using a Cluster Management Tool
-------------------------------------------------

* Tools like PBS (Portable Batch System), Torque, or OpenMPI provide more 
advanced features for managing clusters and running jobs remotely.

Which option do you prefer? Or would you like me to elaborate on any of 
these methods?