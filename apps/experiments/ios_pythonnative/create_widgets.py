from rubicon.objc import ObjCClass, objc_method, SEL

# UIKit classes
UIView = ObjCClass('UIView')
UIButton = ObjCClass('UIButton')
UILabel = ObjCClass('UILabel')
UITextField = ObjCClass('UITextField')
UISwitch = ObjCClass('UISwitch')
UISlider = ObjCClass('UISlider')
UIProgressView = ObjCClass('UIProgressView')
UIStackView = ObjCClass('UIStackView')
UIApplication = ObjCClass('UIApplication')
UIColor = ObjCClass('UIColor')
NSURL = ObjCClass('NSURL')
NSData = ObjCClass('NSData')
UIImage = ObjCClass('UIImage')
UIImageView = ObjCClass('UIImageView')
UIActivityIndicatorView = ObjCClass('UIActivityIndicatorView')

NSObject = ObjCClass('NSObject')


# Create a new class that will handle the button press
class ButtonHandler(NSObject):
    @objc_method
    def buttonTapped_(self, sender):
        sender.setTitle_forState_("Button tapped!", 0)  # 0 represents normal state
        sender.backgroundColor = UIColor.redColor


class SwitchHandler(NSObject):
    @objc_method
    def switchFlipped_(self, sender):
        if sender.isOn:
            sender.superview.backgroundColor = UIColor.greenColor
        else:
            sender.superview.backgroundColor = UIColor.whiteColor


def create_widgets(view_tag):
    app = UIApplication.sharedApplication
    window = app.keyWindow  # Get key window
    root_view = window.viewWithTag_(view_tag)

    # Create UIStackView
    stack_view = UIStackView.new().autorelease()
    stack_view.frame = ((0.0, 0.0), (root_view.frame.size.width,
                                      root_view.frame.size.height * 0.5))  # X, Y, Width, Height
    stack_view.axis = 1  # 1 for vertical orientation
    stack_view.distribution = 0  # 0 for fillEqually
    stack_view.alignment = 0  # 0 for fill
    stack_view.spacing = 10.0
    root_view.addSubview_(stack_view)

    # Create UIImageView
    url = NSURL.URLWithString_("https://source.unsplash.com/450x300/?nature&random=1")
    data = NSData.dataWithContentsOfURL_(url)
    image = UIImage.imageWithData_(data)
    image_view = UIImageView.alloc().initWithImage_(image).autorelease()
    stack_view.addArrangedSubview_(image_view)

    # Create UILabel
    label = UILabel.new().autorelease()
    label.text = "Label created in Python"
    stack_view.addArrangedSubview_(label)

    # Create UIButton
    # handler = ButtonHandler.new().autorelease()
    handler = ButtonHandler.new()
    button = UIButton.new().autorelease()
    button.setTitle_forState_("Button created in Python",
                              0)  # 0 represents normal state
    button.backgroundColor = UIColor.greenColor  # Set the background color to green
    button.setTitleColor_forState_(UIColor.blackColor,
                                   0)  # Set the title color to black for normal state
    button.addTarget_action_forControlEvents_(handler, SEL('buttonTapped:'), 1 << 6)  # 1 << 6 is UIControlEventTouchUpInside
    button.enabled = True
    button.userInteractionEnabled = True
    stack_view.addArrangedSubview_(button)

    # Create UITextField
    text_field = UITextField.new().autorelease()
    text_field.placeholder = "TextField created in Python"
    stack_view.addArrangedSubview_(text_field)

    # Create UISwitch
    switch_handler = SwitchHandler.new()
    switch = UISwitch.new().autorelease()
    switch.addTarget_action_forControlEvents_(switch_handler,
                                              SEL('switchFlipped:'),
                                              1 << 12)  # 1 << 12 is UIControlEventValueChanged
    stack_view.addArrangedSubview_(switch)

    # Create UISlider
    slider = UISlider.new().autorelease()
    stack_view.addArrangedSubview_(slider)

    # Create UIProgressView
    progress_view = UIProgressView.new().autorelease()
    progress_view.progress = 0.66
    stack_view.addArrangedSubview_(progress_view)

    # Create UIActivityIndicatorView
    activity_indicator = UIActivityIndicatorView.new().autorelease()
    activity_indicator.startAnimating()  # Start the animation
    stack_view.addArrangedSubview_(activity_indicator)  # Add to stack view

    # Continue adding other widgets to stack_view as needed...

    return
