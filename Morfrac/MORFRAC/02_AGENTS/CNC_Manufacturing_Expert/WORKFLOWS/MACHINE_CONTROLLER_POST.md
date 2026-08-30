# Machine, controller and post

Capture exact machine ID/model/configuration; travel/envelope; axes/kinematics/limits; table/spindle interface; rpm, power and torque curve; feed/rapid/acceleration; tool capacity; coolant/air; probing; controller/version; supported cycles/codes; precision and known limitations.

Bind the exact machine model and output workplane. Treat a post as validated only for the specified machine/controller/configuration, post revision/hash and tested feature set. Generic or similarly named posts are not production evidence.

Any mismatch, missing validation or unknown coordinate/rotary behaviour sets `MACHINE_CONTROLLER_POST_REQUIRED` or `POSTPROCESSOR_VALIDATION_REQUIRED`.
