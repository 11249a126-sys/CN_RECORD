Aim:

To simulate a network using the Distance Vector routing protocol in NS2 and study packet forwarding when a link fails and is restored.
Algorithm:

78.	Create the NS2 simulator and enable the Distance Vector routing protocol.
79.	Open the NAM and trace output files.
80.	Define a finish procedure to flush and close the trace files and launch NAM.
81.	Create the network nodes.
82.	Connect the nodes using duplex links and set their orientations.
83.	Create a UDP agent and attach it to the source node.
84.	Configure a Constant Bit Rate (CBR) traffic generator and attach it to the UDP agent.
85.	Create a Null agent at the destination and connect it to the UDP agent.
86.	Assign source and destination labels.
87.	Schedule the traffic transmission.
88.	Simulate a link failure and later restore the link.
89.	Stop the traffic, finish the simulation, and observe the routing behaviour.
Program:

# Create simulator
set ns [new Simulator]
 
# Enable Distance Vector routing
$ns rtproto DV
 
# Trace files
set nf [open out.nam w]
$ns namtrace-all $nf
set nt [open trace.tr w]
$ns trace-all $nt
 
# Finish procedure
proc finish {} {
    global ns nf nt
    $ns flush-trace
    close $nf
    close $nt
    exec nam -a out.nam &
    exit 0
}
 
# Create nodes
set n1 [$ns node]
set n2 [$ns node]
set n3 [$ns node]
set n4 [$ns node]
set n5 [$ns node]
set n6 [$ns node]
set n7 [$ns node]
set n8 [$ns node]
 
# Create links
$ns duplex-link $n1 $n2 1Mb 10ms DropTail
$ns duplex-link $n2 $n3 1Mb 10ms DropTail
$ns duplex-link $n3 $n4 1Mb 10ms DropTail
$ns duplex-link $n4 $n5 1Mb 10ms DropTail
$ns duplex-link $n5 $n6 1Mb 10ms DropTail
$ns duplex-link $n6 $n7 1Mb 10ms DropTail
$ns duplex-link $n7 $n8 1Mb 10ms DropTail
$ns duplex-link $n8 $n1 1Mb 10ms DropTail
 
# Link orientation (for NAM)
$ns duplex-link-op $n1 $n2 orient left-up
$ns duplex-link-op $n2 $n3 orient up
$ns duplex-link-op $n3 $n4 orient right-up
$ns duplex-link-op $n4 $n5 orient right
$ns duplex-link-op $n5 $n6 orient right-down
$ns duplex-link-op $n6 $n7 orient down
$ns duplex-link-op $n7 $n8 orient left-down
$ns duplex-link-op $n8 $n1 orient left
 
# UDP Agent
set udp0 [new Agent/UDP]
$ns attach-agent $n1 $udp0
 
# CBR Traffic
set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set interval_ 0.005
$cbr0 attach-agent $udp0
 
# Null Agent (Sink)
set null0 [new Agent/Null]
$ns attach-agent $n4 $null0
 
# Connect UDP to Null
$ns connect $udp0 $null0
 
# Labels
$ns at 0.0 "$n1 label Source"
$ns at 0.0 "$n4 label Destination"
 
# Start traffic
$ns at 0.5 "$cbr0 start"
 
# Link failure and recovery
$ns rtmodel-at 1.0 down $n3 $n4
$ns rtmodel-at 2.0 up $n3 $n4
 
# Stop traffic
$ns at 4.5 "$cbr0 stop"
 
# End simulation
$ns at 5.0 "finish"
 
# Run simulation
$ns run
