Aim:
To simulate a network using the Link State routing protocol in NS2 and observe how packets are routed when network links are disconnected and restored.
Algorithm:
90.	Create an NS2 simulator and open the trace and NAM output files.
91.	Define a finish procedure to flush and close the files and launch NAM.
92.	Create the required network nodes.
93.	Establish duplex links between the nodes to form the network topology.
94.	Create UDP agents at the source nodes and attach CBR traffic applications.
95.	Create Null agents at the destination node and connect the traffic agents.
96.	Enable the Link State routing protocol.
97.	Schedule link failures and link recovery at specified simulation times.
98.	Assign flow identifiers and colours to distinguish the traffic flows.
99.	Schedule the start of traffic and the end of the simulation.
100.	Run the simulation and observe the packet routes in NAM.
Program:

set ns [new Simulator]
set nr [open thro.tr w]
$ns trace-all $nr
set nf [open thro.nam w]
$ns namtrace-all $nf
 
proc finish { } {
    global ns nr nf
    $ns flush-trace
    close $nf
    close $nr
    exec nam thro.nam &
    exit 0
}
 
for { set i 0 } { $i < 12} { incr i 1 } {
    set n($i) [$ns node]
}
 
for {set i 0} {$i < 8} {incr i} {
    $ns duplex-link $n($i) $n([expr $i+1]) 1Mb 10ms DropTail
}
 
$ns duplex-link $n(0) $n(8) 1Mb 10ms DropTail
$ns duplex-link $n(1) $n(10) 1Mb 10ms DropTail
$ns duplex-link $n(0) $n(9) 1Mb 10ms DropTail
$ns duplex-link $n(9) $n(11) 1Mb 10ms DropTail
$ns duplex-link $n(10) $n(11) 1Mb 10ms DropTail
$ns duplex-link $n(11) $n(5) 1Mb 10ms DropTail
 
set udp0 [new Agent/UDP]
$ns attach-agent $n(0) $udp0
 
set cbr0 [new Application/Traffic/CBR]
$cbr0 set packetSize_ 500
$cbr0 set interval_ 0.005
$cbr0 attach-agent $udp0
 
set null0 [new Agent/Null]
$ns attach-agent $n(5) $null0
$ns connect $udp0 $null0
 
set udp1 [new Agent/UDP]
$ns attach-agent $n(1) $udp1
 
set cbr1 [new Application/Traffic/CBR]
$cbr1 set packetSize_ 500
$cbr1 set interval_ 0.005
$cbr1 attach-agent $udp1
 
set null0 [new Agent/Null]
$ns attach-agent $n(5) $null0
$ns connect $udp1 $null0
 
$ns rtproto LS
 
$ns rtmodel-at 10.0 down $n(11) $n(5)
$ns rtmodel-at 15.0 down $n(7) $n(6)
$ns rtmodel-at 30.0 up $n(11) $n(5)
$ns rtmodel-at 20.0 up $n(7) $n(6)
 
$udp0 set fid_ 1
$udp1 set fid_ 2
 
$ns color 1 Red
$ns color 2 Green
 
$ns at 1.0 "$cbr0 start"
$ns at 2.0 "$cbr1 start"
$ns at 45 "finish"
 
$ns run
