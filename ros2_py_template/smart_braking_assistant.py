import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class SmartBrakingAssistant(Node):
    def __init__(self):
        super().__init__('smart_braking_assistant')
        
        # Paraméterek
        self.declare_parameter('max_speed', 5.0)
        self.declare_parameter('safe_distance', 10.0)
        self.declare_parameter('critical_distance', 2.0)
        
        self.max_speed = self.get_parameter('max_speed').value
        self.safe_distance = self.get_parameter('safe_distance').value
        self.critical_distance = self.get_parameter('critical_distance').value
        
        # Subscriber
        self.subscription = self.create_subscription(
            Float32, 'front_distance', self.distance_callback, 10)
        
        self.get_logger().info("Subscriber és paraméterek betöltve.")

    def distance_callback(self, msg):
        self.get_logger().info(f"Új távolsági adat érkezett: {msg.data}m")

def main(args=None):
    rclpy.init(args=args)
    node = SmartBrakingAssistant()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()