{
  "variables": {
    # x265_root as relative path to the module root
    "ffmpeg_root%": "<(module_root_dir)/ffmpeg"
  },
  "targets": [
    { 
      "cflags!": [ "-fno-exceptions" ],
      "cflags_cc!": [ "-fno-exceptions" ],
      "include_dirs" : [
        "<!@(node -p \"require('node-addon-api').include\")",
        "<@(ffmpeg_root)/include"
      ],
      "link_settings": {
        "libraries": [
          "-l:libavcodec.so.58", # temporarily link dynamically
          "-l:libavutil.so.56" # temporarily link dynamically
        ]
      },
      "target_name": "decoder-utility",
      "sources": [
        "native_src/decoder_utility.cc",
        "native_src/decoder.cc"
      ],
      "conditions": [
        ['OS=="mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES'
          }
        }]
      ],
      # To avoid native node modules from throwing cpp exception and raise pending JS exception which can be handled in JS
      "defines": [ 'NAPI_DISABLE_CPP_EXCEPTIONS' ]
    }
  ]
}