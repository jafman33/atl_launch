from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    launchdesc = LaunchDescription([
        DeclareLaunchArgument('PS4', default_value='true'),
    ])

    ##################################
    # NODES STARTED FROM LAUNCH ARGS #
    ##################################

    launchdesc.add_action(Node(
        package='joy',
        executable='joy_node',
        name='PS4_joy',
        # remappings=[('joy', 'teleop/PS4')],
        output='screen',
        # parameters=[
        #     {
        #         'use_sim_time': LaunchConfiguration('use_sim_time'),
        #         'device_name': 'Wireless Controller'
        #     }
        # ],
        condition=IfCondition(LaunchConfiguration('PS4'))
    ))

    return launchdesc
