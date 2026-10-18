from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='smart_braking_assistant',
            executable='smart_braking',
            name='smart_braking_node',
            output='screen',
            parameters=[
                {'max_speed': 5.0},         #ezek a valuek dinamikusan állíthatóak, lásd -> README.md
                {'safe_distance': 10.0},
                {'critical_distance': 2.0}
            ]
        ),
        Node(
            package='smart_braking_assistant',
            executable='simulator',
            name='obstacle_simulator_node',
            output='screen'
        )
    ])
