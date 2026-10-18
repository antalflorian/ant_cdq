import rclpy
from rclpy.node import Node

class SmartBrakingAssistant(Node):
    def __init__(self):
        super().__init__('smart_braking_assistant')
        self.get_logger().info("Smart Braking Assistant elindult, de még üres.")


def main(args=None):
    rclpy.init(args=args)
    node = SmartBrakingAssistant
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
