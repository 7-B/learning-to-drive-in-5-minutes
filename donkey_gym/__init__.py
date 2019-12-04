from gym.envs.registration import register

register(
    id='DonkeyVae-v0',
    entry_point='donkey_gym.vae_env.vae_env:DonkeyVAEEnv',
<<<<<<< HEAD
    max_episode_steps=None,
=======
    timestep_limit=None,
>>>>>>> 68797401f0eadbe936f6351179c1f996f483edf0
)
#
# register(
#     id='donkey-generated-roads-v0',
#     entry_point='donkey_gym.vae_env:GeneratedRoadsEnv',
#     timestep_limit=2000,
# )
#
# register(
#     id='donkey-warehouse-v0',
#     entry_point='donkey_gym.vae_env:WarehouseEnv',
#     timestep_limit=2000,
# )
#
# register(
#     id='donkey-avc-sparkfun-v0',
#     entry_point='donkey_gym.vae_env:AvcSparkfunEnv',
#     timestep_limit=2000,
# )
#
# register(
#     id='donkey-generated-track-v0',
#     entry_point='donkey_gym.vae_env:GeneratedTrackEnv',
#     timestep_limit=2000,
# )
