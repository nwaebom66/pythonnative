//
//  ViewController.swift
//  ios_pythonnative
//
//  Created by Owen Carey on 6/12/23.
//

import UIKit
import Python
import PythonKit

class ViewController: UIViewController {

    override func viewDidLoad() {
        super.viewDidLoad()
        
        guard let stdLibPath = Bundle.main.path(forResource: "python-stdlib", ofType: nil) else {
            print("Could not find path to python-stdlib")
            return
        }
        guard let libDynloadPath = Bundle.main.path(forResource: "python-stdlib/lib-dynload", ofType: nil) else {
            print("Could not find path to python-stdlib/lib-dynload")
            return
        }
                
        setenv("PYTHONHOME", stdLibPath, 1)
        
        // Assuming you've added `rubicon_objc.egg-info` to your app's resources.
        guard let eggInfoPath = Bundle.main.path(forResource: "rubicon_objc.egg-info", ofType: nil) else {
            print("Could not find path to rubicon_objc.egg-info")
            return
        }

        setenv("PYTHONPATH", "\(stdLibPath):\(libDynloadPath):\(eggInfoPath)", 1)
//        setenv("PYTHONPATH", "\(stdLibPath):\(libDynloadPath)", 1)
                
        Py_Initialize()
                
        let sys = Python.import("sys")
        print("Python Version: \(sys.version_info.major).\(sys.version_info.minor)")
        print("Python Encoding: \(sys.getdefaultencoding().upper())")
        print("Python Path: \(sys.path)")
                
        _ = Python.import("math")
        
        // Rubicon
        sys.path.append(Bundle.main.bundlePath)
        let rubicon = Python.import("rubicon")
//        print("Rubicon Version: \(rubicon.__version__)")
        let rubicon_objc = Python.import("rubicon.objc")
        let objcClass = rubicon_objc.ObjCClass
        print(objcClass)
        
//        let createWidgetsModule = Python.import("create_widgets")
//        self.view.tag = 100
//        createWidgetsModule.create_widgets(self.view.tag)
        
//        let mainViewPythonObject = createWidgetsModule.create_widgets()
//
//        print(Python.type(mainViewPythonObject))
//        print(mainViewPythonObject.frame)

        // Convert Python object to UIView
//        if let mainView = mainViewPythonObject as? UIView {
//            self.view.addSubview(mainView)
//        } else {
//            print("Failed to create mainView")
//        }
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        let createWidgetsModule = Python.import("create_widgets")
        self.view.tag = 100
        createWidgetsModule.create_widgets(self.view.tag)
        
        let secondViewController = SecondViewController()
        self.navigationController?.pushViewController(secondViewController, animated: true)
    }

}

