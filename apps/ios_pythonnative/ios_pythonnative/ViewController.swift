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
        setenv("PYTHONPATH", "\(stdLibPath):\(libDynloadPath)", 1)
                
        Py_Initialize()
                
        let sys = Python.import("sys")
        print("Python Version: \(sys.version_info.major).\(sys.version_info.minor)")
        print("Python Encoding: \(sys.getdefaultencoding().upper())")
        print("Python Path: \(sys.path)")
                
        _ = Python.import("math")
    }


}

