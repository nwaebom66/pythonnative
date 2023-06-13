from rubicon.objc import ObjCClass

# UIKit classes
UIView = ObjCClass('UIView')
UIButton = ObjCClass('UIButton')
UILabel = ObjCClass('UILabel')


def create_widgets():
    # Create UIView
    main_view = UIView.new().autorelease()
    main_view.frame = ((0.0, 0.0), (320.0, 480.0)) # X, Y, Width, Height

    # Create UILabel
    label = UILabel.new().autorelease()
    label.frame = ((80.0, 80.0), (160.0, 30.0)) # X, Y, Width, Height
    label.text = "Label created in Python"
    main_view.addSubview_(label)

    # Create UIButton
    button = UIButton.buttonWithType_(UIButton.systemButton())  # systemButton is '0'
    button.frame = ((80.0, 120.0), (160.0, 30.0))  # X, Y, Width, Height
    button.setTitle_forState_("Button created in Python", 0)  # 0 is UIControlStateNormal
    main_view.addSubview_(button)

    return main_view
