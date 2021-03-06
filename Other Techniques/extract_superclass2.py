# by Kami Bigdely
# Extract superclass.


class Shape:
    """Superclass for shape objects"""

    def __init__(self, x, y, visible=True):
        """Initialize variables"""
        self.x = x
        self.y = y
        self.visible = visible

    def display(self):
        """Display the shape"""
        if self.visible:
            print('drew the shape.')

    def set_visible(self, is_visible):
        """Set whether the shape is visible or not"""
        self.visible = is_visible

    def get_center(self):
        """Dummy function to be overridden"""
        pass


class Circle(Shape):
    """Class for Circles"""

    def __init__(self, x, y, r, visible=True):
        """Initialize variables"""
        super().__init__(x, y, visible)
        self.r = r

    def display(self):
        """Draw the Circle"""
        if self.visible:
            print('drew the circle.')

    def get_center(self):
        """Get the center"""
        return self.center_x, self.center_y


class Rectangle(Shape):
    """Class for rectangles"""

    def __init__(self, x, y, width, height, visible=True):
        """Initialize variables"""
        # left-bottom corner.
        super().__init__(x, y, visible)
        self.width = width
        self.height = height

    def display(self):
        """Draw the rectangle"""
        if self.visible:
            print('drew the rectangle.')

    def hide(self):
        """Hide the rectangle"""
        super().set_visible(False)

    def make_visible(self):
        """Show the rectangle"""
        super().set_visible(True)

    def get_center(self):
        """Get the center"""
        return self.x + self.width / 2, \
            self.y + self.height / 2


if __name__ == "__main__":
    circle = Circle(0, 0, 10, False)
    circle.set_visible(True)
    circle.display()
    print('center point', circle.get_center())

    rect = Rectangle(10, 10, 20, 5)
    rect.hide()
    rect.display()  # does not display because it's hidden.
    rect.make_visible()
    rect.display()
    print('center point', rect.get_center())
