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
        
        # Subscriber és Publisher
        self.subscription = self.create_subscription(
            Float32, 'front_distance', self.distance_callback, 10)
        self.publisher_ = self.create_publisher(Float32, 'speed_command', 10)
        
        self.get_logger().info("Smart Braking Assistant teljes logikaval elindult.")

    def distance_callback(self, msg):
        distance = msg.data
        speed_cmd = Float32()
        
        if distance >= self.safe_distance:
            speed_cmd.data = float(self.max_speed)
            self.get_logger().info(f'Tiszta ut: {distance:.2f}m -> Sebesség: {speed_cmd.data:.2f}')
        elif distance > self.critical_distance:
            ratio = (distance - self.critical_distance) / (self.safe_distance - self.critical_distance)
            speed_cmd.data = float(self.max_speed * ratio)
            self.get_logger().warning(f'Lassitas: {distance:.2f}m -> Sebesség: {speed_cmd.data:.2f}')
        else:
            speed_cmd.data = 0.0
            self.get_logger().error(f'VESZFEK: {distance:.2f}m -> Sebesség: 0.0')
            
        self.publisher_.publish(speed_cmd)

def main(args=None):
    rclpy.init(args=args)
    node = SmartBrakingAssistant()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()