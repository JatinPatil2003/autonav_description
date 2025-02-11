#!/usr/bin/python3

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    rviz_config_path = PathJoinSubstitution(
        [FindPackageShare('autonav_navigation'), 'rviz', 'slam.rviz']
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            name='rviz',
            default_value='true',
            description='Run rviz'
        ),

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', rviz_config_path],
            condition=IfCondition(LaunchConfiguration('rviz')),
        )
    ])
