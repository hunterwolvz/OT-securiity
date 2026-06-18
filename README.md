# OT-security

Simple Modbus TCP demonstration showing a basic OT-style client/server setup. The server simulates a PLC-like process exposing a register value (e.g. temperature) and continuously monitors it, while the client connects over the network and writes values directly to that register. The example highlights how Modbus TCP allows unauthenticated write access to process data and how a remote node can override operational values in real time.

# Smart Factory OT Security

This project breaks down how security works in smart factory environments (ICS / OT) and how modern connectivity changes the attack surface. It focuses on how production systems behave, where trust is assumed, and how small compromises can affect physical processes.

A smart factory combines Industrial Control Systems (ICS), Operational Technology (OT), and IT systems to automate and monitor production in real time. It includes robotics, sensors, IoT devices, PLCs, SCADA, MES, and cloud analytics.

The key difference from traditional IT systems is that failures don’t just affect data — they affect physical processes.

In OT environments availability is the priority because production must keep running, integrity is critical because wrong data can cause physical damage, and confidentiality mostly concerns industrial secrets and intellectual property.

A simplified architecture looks like this:

IT / Cloud  
↓  
DMZ  
↓  
SCADA / HMI  
↓  
Industrial Network  
↓  
PLCs  
↓  
Sensors / Actuators  

Critical assets in this environment include PLCs that control machine behaviour, SCADA systems that monitor and display system state, sensors that provide raw input data, engineering workstations used to modify control logic, MES systems that manage production flow, edge and IIoT devices that connect IT and OT, cloud platforms used for analytics, and industrial robots executing physical tasks.

Attack surfaces exist wherever connectivity has been introduced. This includes IIoT devices that are widely distributed and often weakly secured, edge gateways that sit between IT and OT, engineering workstations that have direct access to PLC programming environments, MES systems connected to both business and control layers, cloud dashboards and APIs exposed for remote monitoring, wireless industrial networks that extend beyond physical boundaries, and vendor or third-party remote access that is often trusted by default.

Threats in smart factories are usually not immediate or destructive in a visible way. They tend to manipulate behaviour, data, or decision-making over time. Engineering workstation compromise can lead to PLC logic changes that look legitimate but slowly alter production behaviour. IIoT or sensor manipulation can feed false data into SCADA and MES systems, causing incorrect operational decisions while everything appears normal. MES manipulation can alter production flow without touching machines directly. Cloud or analytics compromise can distort optimisation outputs that influence production at scale. Industrial robot manipulation can introduce small timing or movement changes that accumulate into inefficiency or damage. Ransomware targeting IT and OT bridge systems can remove visibility and control even while physical processes continue running. Wireless exploitation can lead to interception, spoofing, and desynchronisation of systems. Insider threats are especially dangerous because they already operate within trusted boundaries and can make changes that blend in with normal activity.

Common attack paths include engineering workstation compromise leading to PLC logic modification and altered machine behaviour, IIoT compromise leading to false sensor data affecting control systems, IT breaches that allow lateral movement into OT via edge devices, and cloud compromise that feeds incorrect operational data back into MES and decision systems.

A simple example using Modbus shows how this can work in practice. Modbus is widely used in industrial systems but has no authentication, no encryption, and no integrity checks. In a basic setup one device exposes a process value such as temperature, and another device on the same network can overwrite it without restriction. The system accepts the change because it assumes the communication is valid, demonstrating how easily control data can be manipulated when trust is implicit.

Real-world incidents show similar patterns. Stuxnet manipulated PLC logic while hiding real system behaviour from operators. The Ukraine power grid attack involved SCADA compromise and loss of control over critical systems. The Colonial Pipeline incident showed how IT disruption can force OT shutdown due to loss of operational trust.

Security measures in this environment focus on reducing implicit trust and limiting how far a compromise can spread. This includes application whitelisting on engineering systems, strong authentication and role-based access control, network segmentation between IT and OT layers, device identity verification for IIoT systems, encrypted and integrity-checked communication, secure API design in cloud systems, continuous behavioural monitoring rather than only access control, and strict least-privilege access with logging for all user activity.

The main idea is that smart factory security is not just about blocking access. It is about continuously verifying that systems, devices, and data are behaving as expected, because once trusted inputs are manipulated, the system can continue operating normally while producing incorrect or unsafe outcomes.
