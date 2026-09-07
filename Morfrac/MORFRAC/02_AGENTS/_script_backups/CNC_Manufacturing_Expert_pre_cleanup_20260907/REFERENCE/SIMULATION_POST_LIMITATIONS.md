# Simulation and post limitations

Toolpath verification must include cutting moves, leads and links and use the exact cutter/shank/holder with declared clearances. Machine simulation additionally needs accurate machine, fixture, stock, model location and axis configuration.

Autodesk notes that machine collision checks occur at sampled positions and may miss small between-sample collisions; tool-assembly checking also has separate controls. Record such gaps.

The post binds CAM motion to controller-specific NC code. Validate the exact post revision and supported feature set. Independently review the generated code. Neither a green icon nor successful post generation authorises machine transfer or running.
