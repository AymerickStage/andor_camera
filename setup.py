from setuptools import setup

setup(
    name = 'ScopeFoundryHW.Andor_camera',
    
    version = '0.0.1',
    
    description = 'ScopeFoundry Hardware plug-in: Andor camera',
    
    # Author details
    author='Edward S. Barnard',
    author_email='esbarnard@lbl.gov',

    # Choose your license
    license='BSD',

    package_dir={'ScopeFoundryHW.andor_camera': '.'},
    
    packages=['ScopeFoundryHW.andor_camera',],
        
    package_data={
        '':["README", 'LICENSE', # include License and readme 
            "*.ui", # include QT ui files 
            ], 
        },
)
