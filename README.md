# AI Autonomous Pen — Webots V1

Purpose: validate the proposed triangular 3-wheel omnidirectional architecture before buying hardware.

V1 intentionally uses kinematic motion controlled by a Supervisor. It does NOT yet model motor torque, wheel slip, battery, encoders, camera, or handwriting.

Tests:
1. forward
2. backward
3. left
4. right
5. diagonal
6. rotation
7. translation + rotation

Next after this passes:
- replace kinematic motion with real 3-wheel omni kinematics
- add wheel motors and physics
- add pen/paper interaction
- feed handwriting trajectories
