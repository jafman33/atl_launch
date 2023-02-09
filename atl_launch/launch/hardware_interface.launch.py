import pathlib

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    launchdesc = LaunchDescription([
        DeclareLaunchArgument('teensy41', default_value='true'),
    ])

    launchdesc.add_action(Node(
        package='teensy_interface',
        executable='teensy_interface_node',
        output='screen',
        condition=IfCondition(LaunchConfiguration('teensy41'))
    ))

    return launchdesc
