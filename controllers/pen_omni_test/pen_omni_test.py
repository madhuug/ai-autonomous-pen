from controller import Supervisor
import math

robot = Supervisor()
timestep = int(robot.getBasicTimeStep())

translation = robot.getSelf().getField("translation")
rotation = robot.getSelf().getField("rotation")

# This V1 controller is intentionally kinematic:
# it validates the 3-wheel omnidirectional BODY ARCHITECTURE first.
# No motor/torque assumptions yet.

# Desired body-frame commands: vx, vy (m/s), omega (rad/s)
tests = [
    ("forward",  0.030,  0.000,  0.000, 1.8),
    ("backward", -0.030,  0.000,  0.000, 1.8),
    ("left",     0.000,  0.030,  0.000, 1.8),
    ("right",    0.000, -0.030,  0.000, 1.8),
    ("diagonal", 0.025,  0.025,  0.000, 2.0),
    ("rotate",   0.000,  0.000,  1.5,   2.0),
    ("strafe+rot",0.020, 0.000,  1.2,   2.5),
]

def set_pose(x, z, yaw):
    translation.setSFVec3f([x, 0.012, z])
    rotation.setSFRotation([0, 1, 0, yaw])

x, z, yaw = 0.0, 0.0, 0.0
set_pose(x, z, yaw)

step_count = 0
test_index = 0
elapsed = 0.0
last_time = robot.getTime()

while robot.step(timestep) != -1:
    now = robot.getTime()
    dt = now - last_time
    last_time = now
    elapsed += dt

    if test_index >= len(tests):
        # Return to center and stop.
        x, z, yaw = 0.0, 0.0, 0.0
        set_pose(x, z, yaw)
        print("V1 TEST COMPLETE")
        break

    name, vx, vy, omega, duration = tests[test_index]

    # Convert body-frame velocity to world-frame X/Z.
    dx = (vx * math.cos(yaw) - vy * math.sin(yaw)) * dt
    dz = (vx * math.sin(yaw) + vy * math.cos(yaw)) * dt

    x += dx
    z += dz
    yaw += omega * dt

    set_pose(x, z, yaw)

    if elapsed >= duration:
        print(f"TEST {test_index + 1}/{len(tests)}: {name} complete")
        test_index += 1
        elapsed = 0.0
