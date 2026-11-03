Aim:
To simulate TCP and UDP traffic in a network topology using the NS2 network simulator and observe packet transmission.
Algorithm:
68.	Create an NS2 simulator object and assign colours for the traffic flows.
69.	Open the NAM trace file and define the procedure to finish the simulation.
70.	Create the required network nodes and establish duplex links between them.
71.	Set the queue limit and link orientation for visualization.
72.	Create and attach a TCP agent and TCP sink to the source and destination nodes.
73.	Connect the TCP agent to the sink and attach an FTP application.
74.	Create and attach a UDP agent and Null agent, then connect them.
75.	Configure a CBR application over UDP with the required packet size and rate.
76.	Schedule the start and stop times of the TCP and UDP traffic.
77.	Run the simulation and view the network animation in NAM.
Program:

# Create simulator
set ns [new Simulator]
 
# Define colors
$ns color 1 Blue
$ns color 2 Red
 
# Open NAM trace file
set nf [open out.nam w]
$ns namtrace-all $nf
 
# Finish procedure
proc finish {} {
    global ns nf
    $ns flush-trace
    close $nf
    exec nam out.nam &
    exit 0
}
 
# Create nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
 
# Create links
$ns duplex-link $n0 $n2 2Mb 10ms DropTail
$ns duplex-link $n1 $n2 2Mb 10ms DropTail
$ns duplex-link $n2 $n3 1.7Mb 20ms DropTail
 
# Queue limit
$ns queue-limit $n2 $n3 10
 
# Link orientation (for NAM)
$ns duplex-link-op $n0 $n2 orient right-down
$ns duplex-link-op $n1 $n2 orient right-up
$ns duplex-link-op $n2 $n3 orient right
$ns duplex-link-op $n2 $n3 queuePos 0.5
 
# TCP setup
set tcp [new Agent/TCP]
$tcp set class_ 2
$tcp set fid_ 1
 
$ns attach-agent $n0 $tcp
 
set sink [new Agent/TCPSink]
$ns attach-agent $n3 $sink
 
$ns connect $tcp $sink
 
# FTP over TCP
set ftp [new Application/FTP]
$ftp attach-agent $tcp
$ftp set type_ FTP
 
# UDP setup
set udp [new Agent/UDP]
$udp set fid_ 2
$ns attach-agent $n1 $udp
 
set null [new Agent/Null]
$ns attach-agent $n3 $null
 
$ns connect $udp $null
 
# CBR over UDP
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set type_ CBR
$cbr set packet_size_ 1000
$cbr set rate_ 1mb
$cbr set random_ false
 
# Scheduling events
$ns at 0.1 "$cbr start"
$ns at 1.0 "$ftp start"
$ns at 4.0 "$ftp stop"
$ns at 4.5 "$cbr stop"
 
# Detach agents
$ns at 4.5 "$ns detach-agent $n0 $tcp"
$ns at 4.5 "$ns detach-agent $n3 $sink"
 
# End simulation
$ns at 5.0 "finish"
 
# Print values
puts "CBR packet size = [$cbr set packet_size_]"
puts "CBR interval = [$cbr set interval_]"
 
# Run simulation
$ns run
