from rubicon.objc import ObjCClass, ObjCInstance

# UIKit classes
UIView = ObjCClass('UIView')
UIButton = ObjCClass('UIButton')
UILabel = ObjCClass('UILabel')
UIApplication = ObjCClass('UIApplication')


def create_widgets(view_tag):
    app = UIApplication.sharedApplication
    window = app.keyWindow  # Get key window
    root_view = window.viewWithTag_(view_tag)
    
    # Create UILabel
    label = UILabel.new().autorelease()
    label.frame = ((80.0, 80.0), (160.0, 30.0)) # X, Y, Width, Height
    label.text = "Label created in Python"
    label.sizeToFit()
    root_view.addSubview_(label)

    # Continue adding other widgets to root_view as needed...

    return
