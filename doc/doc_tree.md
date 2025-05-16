.
├── data
│   ├── audio
│   │   ├── demo
│   │   │   ├── demo1.wav
│   │   │   └── demo2.wav
│   │   ├── full_audio.m4a
│   │   ├── Isha Kriya.mp3
│   │   └── test.wav
│   └── output_clips
│       ├── clip_001.wav
│       ├── clip_002.wav
│       ├── clip_003.wav
│       ├── clip_004.wav
│       ├── clip_005.wav
│       ├── clip_006.wav
│       ├── clip_007.wav
│       ├── clip_008.wav
│       ├── clip_009.wav
│       ├── clip_010.wav
│       ├── clip_011.wav
│       ├── clip_012.wav
│       ├── clip_013.wav
│       ├── clip_014.wav
│       ├── clip_015.wav
│       ├── clip_016.wav
│       ├── clip_017.wav
│       ├── clip_018.wav
│       ├── clip_019.wav
│       ├── clip_020.wav
│       ├── clip_021.wav
│       ├── clip_022.wav
│       ├── clip_023.wav
│       ├── clip_024.wav
│       ├── clip_025.wav
│       ├── clip_026.wav
│       ├── clip_027.wav
│       ├── clip_028.wav
│       ├── clip_029.wav
│       ├── clip_030.wav
│       ├── clip_031.wav
│       ├── clip_032.wav
│       ├── clip_033.wav
│       ├── clip_034.wav
│       ├── clip_035.wav
│       ├── clip_036.wav
│       ├── clip_037.wav
│       ├── clip_038.wav
│       ├── clip_039.wav
│       ├── clip_040.wav
│       ├── clip_041.wav
│       ├── clip_042.wav
│       ├── clip_043.wav
│       ├── clip_044.wav
│       ├── clip_045.wav
│       ├── clip_046.wav
│       ├── clip_047.wav
│       ├── clip_048.wav
│       ├── clip_049.wav
│       ├── clip_050.wav
│       ├── clip_051.wav
│       ├── clip_052.wav
│       ├── clip_053.wav
│       ├── clip_054.wav
│       ├── clip_055.wav
│       ├── clip_056.wav
│       ├── clip_057.wav
│       ├── clip_058.wav
│       ├── clip_059.wav
│       ├── clip_060.wav
│       ├── clip_061.wav
│       ├── clip_062.wav
│       ├── clip_063.wav
│       ├── clip_064.wav
│       ├── clip_065.wav
│       ├── clip_066.wav
│       ├── clip_067.wav
│       ├── clip_068.wav
│       ├── clip_069.wav
│       ├── clip_070.wav
│       ├── clip_071.wav
│       ├── clip_072.wav
│       ├── clip_073.wav
│       ├── clip_074.wav
│       ├── clip_075.wav
│       ├── clip_076.wav
│       ├── clip_077.wav
│       ├── clip_078.wav
│       ├── clip_079.wav
│       ├── clip_080.wav
│       ├── clip_081.wav
│       ├── clip_082.wav
│       ├── clip_083.wav
│       ├── clip_084.wav
│       ├── clip_085.wav
│       ├── clip_086.wav
│       ├── clip_087.wav
│       ├── clip_088.wav
│       ├── clip_089.wav
│       ├── clip_090.wav
│       ├── clip_091.wav
│       ├── clip_092.wav
│       ├── clip_093.wav
│       ├── clip_094.wav
│       ├── clip_095.wav
│       ├── clip_096.wav
│       ├── clip_097.wav
│       ├── clip_098.wav
│       ├── clip_099.wav
│       ├── clip_100.wav
│       ├── clip_101.wav
│       ├── clip_102.wav
│       ├── clip_103.wav
│       ├── clip_104.wav
│       ├── converted.wav
│       └── timestamps.txt
├── doc
│   └── doc_tree.md
├── notebooks
│   ├── gen_folder_transcripts.ipynb
│   ├── gen_transcript.ipynb
│   ├── temporary_storage.ipynb
│   ├── whisper.ipynb
│   └── yt_audio_workflow.ipynb
├── pyproject.toml
├── README.md
├── scripts
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-312.pyc
│   │   ├── env.cpython-312.pyc
│   │   ├── time_stamp_cleaner.cpython-312.pyc
│   │   └── voice2transcripts.cpython-312.pyc
│   ├── env.py
│   ├── time_stamp_cleaner.py
│   ├── transcripts_summary.py
│   ├── voice2transcripts.py
│   └── yt_mp3_download.py
├── spec
│   ├── spec_cli.md
│   └── spec_read_add.md
├── test
│   ├── __pycache__
│   │   ├── test_time_stamp_cleaner.cpython-312-pytest-8.3.5.pyc
│   │   ├── test_voice2transcripts.cpython-312-pytest-8.3.5.pyc
│   │   └── test_whisper_cpp.cpython-312-pytest-8.3.5.pyc
│   ├── test_time_stamp_cleaner.py
│   ├── test_voice2transcripts.py
│   └── test_whisper_cpp.py
├── uv.lock
└── whisper.cpp
    ├── AUTHORS
    ├── bindings
    │   ├── CMakeLists.txt
    │   ├── go
    │   │   ├── doc.go
    │   │   ├── examples
    │   │   │   ├── go-model-download
    │   │   │   │   ├── context.go
    │   │   │   │   └── main.go
    │   │   │   └── go-whisper
    │   │   │       ├── color.go
    │   │   │       ├── flags.go
    │   │   │       ├── main.go
    │   │   │       └── process.go
    │   │   ├── go.mod
    │   │   ├── go.sum
    │   │   ├── LICENSE
    │   │   ├── Makefile
    │   │   ├── params.go
    │   │   ├── pkg
    │   │   │   └── whisper
    │   │   │       ├── consts.go
    │   │   │       ├── context_test.go
    │   │   │       ├── context.go
    │   │   │       ├── doc.go
    │   │   │       ├── interface.go
    │   │   │       ├── model_test.go
    │   │   │       ├── model.go
    │   │   │       └── util_test.go
    │   │   ├── README.md
    │   │   ├── samples
    │   │   │   └── jfk.wav
    │   │   ├── whisper_test.go
    │   │   └── whisper.go
    │   ├── java
    │   │   ├── build.gradle
    │   │   ├── gradle
    │   │   │   └── wrapper
    │   │   │       ├── gradle-wrapper.jar
    │   │   │       └── gradle-wrapper.properties
    │   │   ├── gradle.properties
    │   │   ├── gradlew
    │   │   ├── gradlew.bat
    │   │   ├── README.md
    │   │   ├── settings.gradle
    │   │   └── src
    │   │       ├── main
    │   │       │   └── java
    │   │       │       └── io
    │   │       │           └── github
    │   │       │               └── ggerganov
    │   │       │                   └── whispercpp
    │   │       │                       ├── bean
    │   │       │                       │   └── WhisperSegment.java
    │   │       │                       ├── callbacks
    │   │       │                       │   ├── GgmlAbortCallback.java
    │   │       │                       │   ├── WhisperEncoderBeginCallback.java
    │   │       │                       │   ├── WhisperLogitsFilterCallback.java
    │   │       │                       │   ├── WhisperNewSegmentCallback.java
    │   │       │                       │   └── WhisperProgressCallback.java
    │   │       │                       ├── ggml
    │   │       │                       │   ├── GgmlTensor.java
    │   │       │                       │   └── GgmlType.java
    │   │       │                       ├── model
    │   │       │                       │   ├── EModel.java
    │   │       │                       │   ├── WhisperModel.java
    │   │       │                       │   ├── WhisperModelLoader.java
    │   │       │                       │   ├── WhisperState.java
    │   │       │                       │   └── WhisperTokenData.java
    │   │       │                       ├── params
    │   │       │                       │   ├── BeamSearchParams.java
    │   │       │                       │   ├── CBool.java
    │   │       │                       │   ├── GreedyParams.java
    │   │       │                       │   ├── WhisperAhead.java
    │   │       │                       │   ├── WhisperAheads.java
    │   │       │                       │   ├── WhisperContextParams.java
    │   │       │                       │   ├── WhisperFilters.java
    │   │       │                       │   ├── WhisperFullParams.java
    │   │       │                       │   ├── WhisperHParams.java
    │   │       │                       │   └── WhisperSamplingStrategy.java
    │   │       │                       ├── WhisperConstants.java
    │   │       │                       ├── WhisperContext.java
    │   │       │                       ├── WhisperCpp.java
    │   │       │                       └── WhisperCppJnaLibrary.java
    │   │       └── test
    │   │           └── java
    │   │               └── io
    │   │                   └── github
    │   │                       └── ggerganov
    │   │                           └── whispercpp
    │   │                               ├── WhisperCppTest.java
    │   │                               └── WhisperJnaLibraryTest.java
    │   ├── javascript
    │   │   ├── CMakeLists.txt
    │   │   ├── emscripten.cpp
    │   │   ├── libwhisper.worker.js
    │   │   ├── package-tmpl.json
    │   │   ├── package.json
    │   │   ├── README.md
    │   │   └── whisper.js
    │   └── ruby
    │       ├── ext
    │       │   ├── dependencies.rb
    │       │   ├── extconf.rb
    │       │   ├── options.rb
    │       │   ├── ruby_whisper_context.c
    │       │   ├── ruby_whisper_error.c
    │       │   ├── ruby_whisper_model.c
    │       │   ├── ruby_whisper_params.c
    │       │   ├── ruby_whisper_segment.c
    │       │   ├── ruby_whisper_transcribe.cpp
    │       │   ├── ruby_whisper.c
    │       │   ├── ruby_whisper.h
    │       │   └── sources
    │       │       └── CMakeGraphVizOptions.cmake
    │       ├── extsources.rb
    │       ├── lib
    │       │   └── whisper
    │       │       └── model
    │       │           └── uri.rb
    │       ├── Rakefile
    │       ├── README.md
    │       ├── sig
    │       │   └── whisper.rbs
    │       ├── tests
    │       │   ├── helper.rb
    │       │   ├── jfk_reader
    │       │   │   ├── extconf.rb
    │       │   │   └── jfk_reader.c
    │       │   ├── test_callback.rb
    │       │   ├── test_error.rb
    │       │   ├── test_model.rb
    │       │   ├── test_package.rb
    │       │   ├── test_params.rb
    │       │   ├── test_segment.rb
    │       │   └── test_whisper.rb
    │       └── whispercpp.gemspec
    ├── build
    │   ├── autogenerated
    │   │   ├── ggml-metal-embed.metal
    │   │   ├── ggml-metal-embed.metal.tmp
    │   │   └── ggml-metal-embed.s
    │   ├── bin
    │   │   ├── bench
    │   │   ├── ggml-common.h
    │   │   ├── ggml-metal-impl.h
    │   │   ├── ggml-metal.metal
    │   │   ├── main
    │   │   ├── quantize
    │   │   ├── test-vad
    │   │   ├── test-vad-full
    │   │   ├── vad-speech-segments
    │   │   ├── whisper-bench
    │   │   ├── whisper-cli
    │   │   └── whisper-server
    │   ├── cmake_install.cmake
    │   ├── CMakeCache.txt
    │   ├── CMakeFiles
    │   │   ├── 4.0.2
    │   │   │   ├── CMakeASMCompiler.cmake
    │   │   │   ├── CMakeCCompiler.cmake
    │   │   │   ├── CMakeCXXCompiler.cmake
    │   │   │   ├── CMakeDetermineCompilerABI_C.bin
    │   │   │   ├── CMakeDetermineCompilerABI_CXX.bin
    │   │   │   ├── CMakeSystem.cmake
    │   │   │   ├── CompilerIdASM
    │   │   │   ├── CompilerIdC
    │   │   │   │   ├── a.out
    │   │   │   │   ├── apple-sdk.c
    │   │   │   │   ├── CMakeCCompilerId.c
    │   │   │   │   └── tmp
    │   │   │   └── CompilerIdCXX
    │   │   │       ├── a.out
    │   │   │       ├── apple-sdk.cpp
    │   │   │       ├── CMakeCXXCompilerId.cpp
    │   │   │       └── tmp
    │   │   ├── cmake.check_cache
    │   │   ├── CMakeConfigureLog.yaml
    │   │   ├── CMakeDirectoryInformation.cmake
    │   │   ├── CMakeRuleHashes.txt
    │   │   ├── CMakeScratch
    │   │   ├── Continuous.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ContinuousBuild.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ContinuousConfigure.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ContinuousCoverage.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ContinuousMemCheck.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ContinuousStart.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ContinuousSubmit.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ContinuousTest.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ContinuousUpdate.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── Experimental.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ExperimentalBuild.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ExperimentalConfigure.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ExperimentalCoverage.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ExperimentalMemCheck.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ExperimentalStart.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ExperimentalSubmit.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ExperimentalTest.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── ExperimentalUpdate.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── InstallScripts.json
    │   │   ├── Makefile.cmake
    │   │   ├── Makefile2
    │   │   ├── Nightly.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── NightlyBuild.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── NightlyConfigure.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── NightlyCoverage.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── NightlyMemCheck.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── NightlyMemoryCheck.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── NightlyStart.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── NightlySubmit.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── NightlyTest.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── NightlyUpdate.dir
    │   │   │   ├── build.make
    │   │   │   ├── cmake_clean.cmake
    │   │   │   ├── compiler_depend.make
    │   │   │   ├── compiler_depend.ts
    │   │   │   ├── DependInfo.cmake
    │   │   │   └── progress.make
    │   │   ├── pkgRedirects
    │   │   ├── progress.marks
    │   │   └── TargetDirectories.txt
    │   ├── compile_commands.json
    │   ├── CTestTestfile.cmake
    │   ├── DartConfiguration.tcl
    │   ├── examples
    │   │   ├── bench
    │   │   │   ├── cmake_install.cmake
    │   │   │   ├── CMakeFiles
    │   │   │   │   ├── CMakeDirectoryInformation.cmake
    │   │   │   │   ├── progress.marks
    │   │   │   │   └── whisper-bench.dir
    │   │   │   │       ├── bench.cpp.o
    │   │   │   │       ├── bench.cpp.o.d
    │   │   │   │       ├── build.make
    │   │   │   │       ├── cmake_clean.cmake
    │   │   │   │       ├── compiler_depend.make
    │   │   │   │       ├── compiler_depend.ts
    │   │   │   │       ├── depend.make
    │   │   │   │       ├── DependInfo.cmake
    │   │   │   │       ├── flags.make
    │   │   │   │       ├── link.txt
    │   │   │   │       └── progress.make
    │   │   │   ├── CTestTestfile.cmake
    │   │   │   └── Makefile
    │   │   ├── cli
    │   │   │   ├── cmake_install.cmake
    │   │   │   ├── CMakeFiles
    │   │   │   │   ├── CMakeDirectoryInformation.cmake
    │   │   │   │   ├── progress.marks
    │   │   │   │   └── whisper-cli.dir
    │   │   │   │       ├── build.make
    │   │   │   │       ├── cli.cpp.o
    │   │   │   │       ├── cli.cpp.o.d
    │   │   │   │       ├── cmake_clean.cmake
    │   │   │   │       ├── compiler_depend.make
    │   │   │   │       ├── compiler_depend.ts
    │   │   │   │       ├── depend.make
    │   │   │   │       ├── DependInfo.cmake
    │   │   │   │       ├── flags.make
    │   │   │   │       ├── link.txt
    │   │   │   │       └── progress.make
    │   │   │   ├── CTestTestfile.cmake
    │   │   │   └── Makefile
    │   │   ├── cmake_install.cmake
    │   │   ├── CMakeFiles
    │   │   │   ├── CMakeDirectoryInformation.cmake
    │   │   │   ├── common.dir
    │   │   │   │   ├── build.make
    │   │   │   │   ├── cmake_clean_target.cmake
    │   │   │   │   ├── cmake_clean.cmake
    │   │   │   │   ├── common-ggml.cpp.o
    │   │   │   │   ├── common-ggml.cpp.o.d
    │   │   │   │   ├── common-whisper.cpp.o
    │   │   │   │   ├── common-whisper.cpp.o.d
    │   │   │   │   ├── common.cpp.o
    │   │   │   │   ├── common.cpp.o.d
    │   │   │   │   ├── compiler_depend.make
    │   │   │   │   ├── compiler_depend.ts
    │   │   │   │   ├── depend.make
    │   │   │   │   ├── DependInfo.cmake
    │   │   │   │   ├── flags.make
    │   │   │   │   ├── grammar-parser.cpp.o
    │   │   │   │   ├── grammar-parser.cpp.o.d
    │   │   │   │   ├── link.txt
    │   │   │   │   └── progress.make
    │   │   │   └── progress.marks
    │   │   ├── CTestTestfile.cmake
    │   │   ├── deprecation-warning
    │   │   │   ├── cmake_install.cmake
    │   │   │   ├── CMakeFiles
    │   │   │   │   ├── bench.dir
    │   │   │   │   │   ├── build.make
    │   │   │   │   │   ├── cmake_clean.cmake
    │   │   │   │   │   ├── compiler_depend.make
    │   │   │   │   │   ├── compiler_depend.ts
    │   │   │   │   │   ├── depend.make
    │   │   │   │   │   ├── DependInfo.cmake
    │   │   │   │   │   ├── deprecation-warning.cpp.o
    │   │   │   │   │   ├── deprecation-warning.cpp.o.d
    │   │   │   │   │   ├── flags.make
    │   │   │   │   │   ├── link.txt
    │   │   │   │   │   └── progress.make
    │   │   │   │   ├── CMakeDirectoryInformation.cmake
    │   │   │   │   ├── main.dir
    │   │   │   │   │   ├── build.make
    │   │   │   │   │   ├── cmake_clean.cmake
    │   │   │   │   │   ├── compiler_depend.make
    │   │   │   │   │   ├── compiler_depend.ts
    │   │   │   │   │   ├── depend.make
    │   │   │   │   │   ├── DependInfo.cmake
    │   │   │   │   │   ├── deprecation-warning.cpp.o
    │   │   │   │   │   ├── deprecation-warning.cpp.o.d
    │   │   │   │   │   ├── flags.make
    │   │   │   │   │   ├── link.txt
    │   │   │   │   │   └── progress.make
    │   │   │   │   └── progress.marks
    │   │   │   ├── CTestTestfile.cmake
    │   │   │   └── Makefile
    │   │   ├── libcommon.a
    │   │   ├── Makefile
    │   │   ├── quantize
    │   │   │   ├── cmake_install.cmake
    │   │   │   ├── CMakeFiles
    │   │   │   │   ├── CMakeDirectoryInformation.cmake
    │   │   │   │   ├── progress.marks
    │   │   │   │   └── quantize.dir
    │   │   │   │       ├── build.make
    │   │   │   │       ├── cmake_clean.cmake
    │   │   │   │       ├── compiler_depend.make
    │   │   │   │       ├── compiler_depend.ts
    │   │   │   │       ├── depend.make
    │   │   │   │       ├── DependInfo.cmake
    │   │   │   │       ├── flags.make
    │   │   │   │       ├── link.txt
    │   │   │   │       ├── progress.make
    │   │   │   │       ├── quantize.cpp.o
    │   │   │   │       └── quantize.cpp.o.d
    │   │   │   ├── CTestTestfile.cmake
    │   │   │   └── Makefile
    │   │   ├── server
    │   │   │   ├── cmake_install.cmake
    │   │   │   ├── CMakeFiles
    │   │   │   │   ├── CMakeDirectoryInformation.cmake
    │   │   │   │   ├── progress.marks
    │   │   │   │   └── whisper-server.dir
    │   │   │   │       ├── build.make
    │   │   │   │       ├── cmake_clean.cmake
    │   │   │   │       ├── compiler_depend.make
    │   │   │   │       ├── compiler_depend.ts
    │   │   │   │       ├── depend.make
    │   │   │   │       ├── DependInfo.cmake
    │   │   │   │       ├── flags.make
    │   │   │   │       ├── link.txt
    │   │   │   │       ├── progress.make
    │   │   │   │       ├── server.cpp.o
    │   │   │   │       └── server.cpp.o.d
    │   │   │   ├── CTestTestfile.cmake
    │   │   │   └── Makefile
    │   │   └── vad-speech-segments
    │   │       ├── cmake_install.cmake
    │   │       ├── CMakeFiles
    │   │       │   ├── CMakeDirectoryInformation.cmake
    │   │       │   ├── progress.marks
    │   │       │   └── vad-speech-segments.dir
    │   │       │       ├── build.make
    │   │       │       ├── cmake_clean.cmake
    │   │       │       ├── compiler_depend.make
    │   │       │       ├── compiler_depend.ts
    │   │       │       ├── depend.make
    │   │       │       ├── DependInfo.cmake
    │   │       │       ├── flags.make
    │   │       │       ├── link.txt
    │   │       │       ├── progress.make
    │   │       │       ├── speech.cpp.o
    │   │       │       └── speech.cpp.o.d
    │   │       ├── CTestTestfile.cmake
    │   │       └── Makefile
    │   ├── ggml
    │   │   ├── cmake_install.cmake
    │   │   ├── CMakeFiles
    │   │   │   ├── CMakeDirectoryInformation.cmake
    │   │   │   └── progress.marks
    │   │   ├── ggml-config.cmake
    │   │   ├── ggml-version.cmake
    │   │   ├── Makefile
    │   │   └── src
    │   │       ├── cmake_install.cmake
    │   │       ├── CMakeFiles
    │   │       │   ├── CMakeDirectoryInformation.cmake
    │   │       │   ├── ggml-base.dir
    │   │       │   │   ├── build.make
    │   │       │   │   ├── cmake_clean.cmake
    │   │       │   │   ├── compiler_depend.make
    │   │       │   │   ├── compiler_depend.ts
    │   │       │   │   ├── depend.make
    │   │       │   │   ├── DependInfo.cmake
    │   │       │   │   ├── flags.make
    │   │       │   │   ├── ggml-alloc.c.o
    │   │       │   │   ├── ggml-alloc.c.o.d
    │   │       │   │   ├── ggml-backend.cpp.o
    │   │       │   │   ├── ggml-backend.cpp.o.d
    │   │       │   │   ├── ggml-opt.cpp.o
    │   │       │   │   ├── ggml-opt.cpp.o.d
    │   │       │   │   ├── ggml-quants.c.o
    │   │       │   │   ├── ggml-quants.c.o.d
    │   │       │   │   ├── ggml-threading.cpp.o
    │   │       │   │   ├── ggml-threading.cpp.o.d
    │   │       │   │   ├── ggml.c.o
    │   │       │   │   ├── ggml.c.o.d
    │   │       │   │   ├── gguf.cpp.o
    │   │       │   │   ├── gguf.cpp.o.d
    │   │       │   │   ├── link.txt
    │   │       │   │   └── progress.make
    │   │       │   ├── ggml-cpu.dir
    │   │       │   │   ├── build.make
    │   │       │   │   ├── cmake_clean.cmake
    │   │       │   │   ├── compiler_depend.make
    │   │       │   │   ├── compiler_depend.ts
    │   │       │   │   ├── depend.make
    │   │       │   │   ├── DependInfo.cmake
    │   │       │   │   ├── flags.make
    │   │       │   │   ├── ggml-cpu
    │   │       │   │   │   ├── amx
    │   │       │   │   │   │   ├── amx.cpp.o
    │   │       │   │   │   │   ├── amx.cpp.o.d
    │   │       │   │   │   │   ├── mmq.cpp.o
    │   │       │   │   │   │   └── mmq.cpp.o.d
    │   │       │   │   │   ├── binary-ops.cpp.o
    │   │       │   │   │   ├── binary-ops.cpp.o.d
    │   │       │   │   │   ├── ggml-cpu-aarch64.cpp.o
    │   │       │   │   │   ├── ggml-cpu-aarch64.cpp.o.d
    │   │       │   │   │   ├── ggml-cpu-hbm.cpp.o
    │   │       │   │   │   ├── ggml-cpu-hbm.cpp.o.d
    │   │       │   │   │   ├── ggml-cpu-quants.c.o
    │   │       │   │   │   ├── ggml-cpu-quants.c.o.d
    │   │       │   │   │   ├── ggml-cpu-traits.cpp.o
    │   │       │   │   │   ├── ggml-cpu-traits.cpp.o.d
    │   │       │   │   │   ├── ggml-cpu.c.o
    │   │       │   │   │   ├── ggml-cpu.c.o.d
    │   │       │   │   │   ├── ggml-cpu.cpp.o
    │   │       │   │   │   ├── ggml-cpu.cpp.o.d
    │   │       │   │   │   ├── ops.cpp.o
    │   │       │   │   │   ├── ops.cpp.o.d
    │   │       │   │   │   ├── unary-ops.cpp.o
    │   │       │   │   │   ├── unary-ops.cpp.o.d
    │   │       │   │   │   ├── vec.cpp.o
    │   │       │   │   │   └── vec.cpp.o.d
    │   │       │   │   ├── link.txt
    │   │       │   │   └── progress.make
    │   │       │   ├── ggml.dir
    │   │       │   │   ├── build.make
    │   │       │   │   ├── cmake_clean.cmake
    │   │       │   │   ├── compiler_depend.make
    │   │       │   │   ├── compiler_depend.ts
    │   │       │   │   ├── depend.make
    │   │       │   │   ├── DependInfo.cmake
    │   │       │   │   ├── flags.make
    │   │       │   │   ├── ggml-backend-reg.cpp.o
    │   │       │   │   ├── ggml-backend-reg.cpp.o.d
    │   │       │   │   ├── link.txt
    │   │       │   │   └── progress.make
    │   │       │   └── progress.marks
    │   │       ├── ggml-blas
    │   │       │   ├── cmake_install.cmake
    │   │       │   ├── CMakeFiles
    │   │       │   │   ├── CMakeDirectoryInformation.cmake
    │   │       │   │   ├── ggml-blas.dir
    │   │       │   │   │   ├── build.make
    │   │       │   │   │   ├── cmake_clean.cmake
    │   │       │   │   │   ├── compiler_depend.make
    │   │       │   │   │   ├── compiler_depend.ts
    │   │       │   │   │   ├── depend.make
    │   │       │   │   │   ├── DependInfo.cmake
    │   │       │   │   │   ├── flags.make
    │   │       │   │   │   ├── ggml-blas.cpp.o
    │   │       │   │   │   ├── ggml-blas.cpp.o.d
    │   │       │   │   │   ├── link.txt
    │   │       │   │   │   └── progress.make
    │   │       │   │   └── progress.marks
    │   │       │   ├── libggml-blas.dylib
    │   │       │   └── Makefile
    │   │       ├── ggml-cpu
    │   │       │   ├── cmake_install.cmake
    │   │       │   ├── CMakeFiles
    │   │       │   │   ├── CMakeDirectoryInformation.cmake
    │   │       │   │   └── progress.marks
    │   │       │   └── Makefile
    │   │       ├── ggml-metal
    │   │       │   ├── cmake_install.cmake
    │   │       │   ├── CMakeFiles
    │   │       │   │   ├── CMakeDirectoryInformation.cmake
    │   │       │   │   ├── ggml-metal.dir
    │   │       │   │   │   ├── __
    │   │       │   │   │   │   └── __
    │   │       │   │   │   │       └── __
    │   │       │   │   │   │           └── autogenerated
    │   │       │   │   │   │               └── ggml-metal-embed.s.o
    │   │       │   │   │   ├── ASM.includecache
    │   │       │   │   │   ├── build.make
    │   │       │   │   │   ├── cmake_clean.cmake
    │   │       │   │   │   ├── compiler_depend.make
    │   │       │   │   │   ├── compiler_depend.ts
    │   │       │   │   │   ├── depend.internal
    │   │       │   │   │   ├── depend.make
    │   │       │   │   │   ├── DependInfo.cmake
    │   │       │   │   │   ├── flags.make
    │   │       │   │   │   ├── ggml-metal.m.o
    │   │       │   │   │   ├── ggml-metal.m.o.d
    │   │       │   │   │   ├── link.txt
    │   │       │   │   │   └── progress.make
    │   │       │   │   └── progress.marks
    │   │       │   ├── libggml-metal.dylib
    │   │       │   └── Makefile
    │   │       ├── libggml-base.dylib
    │   │       ├── libggml-cpu.dylib
    │   │       ├── libggml.dylib
    │   │       └── Makefile
    │   ├── Makefile
    │   ├── src
    │   │   ├── cmake_install.cmake
    │   │   ├── CMakeFiles
    │   │   │   ├── CMakeDirectoryInformation.cmake
    │   │   │   ├── progress.marks
    │   │   │   └── whisper.dir
    │   │   │       ├── build.make
    │   │   │       ├── cmake_clean.cmake
    │   │   │       ├── compiler_depend.make
    │   │   │       ├── compiler_depend.ts
    │   │   │       ├── depend.make
    │   │   │       ├── DependInfo.cmake
    │   │   │       ├── flags.make
    │   │   │       ├── link.txt
    │   │   │       ├── progress.make
    │   │   │       ├── whisper.cpp.o
    │   │   │       └── whisper.cpp.o.d
    │   │   ├── libwhisper.1.7.5.dylib
    │   │   ├── libwhisper.1.dylib -> libwhisper.1.7.5.dylib
    │   │   ├── libwhisper.dylib -> libwhisper.1.dylib
    │   │   └── Makefile
    │   ├── Testing
    │   │   └── Temporary
    │   ├── tests
    │   │   ├── cmake_install.cmake
    │   │   ├── CMakeFiles
    │   │   │   ├── CMakeDirectoryInformation.cmake
    │   │   │   ├── progress.marks
    │   │   │   ├── test-vad-full.dir
    │   │   │   │   ├── build.make
    │   │   │   │   ├── cmake_clean.cmake
    │   │   │   │   ├── compiler_depend.make
    │   │   │   │   ├── compiler_depend.ts
    │   │   │   │   ├── depend.make
    │   │   │   │   ├── DependInfo.cmake
    │   │   │   │   ├── flags.make
    │   │   │   │   ├── link.txt
    │   │   │   │   ├── progress.make
    │   │   │   │   ├── test-vad-full.cpp.o
    │   │   │   │   └── test-vad-full.cpp.o.d
    │   │   │   └── test-vad.dir
    │   │   │       ├── build.make
    │   │   │       ├── cmake_clean.cmake
    │   │   │       ├── compiler_depend.make
    │   │   │       ├── compiler_depend.ts
    │   │   │       ├── depend.make
    │   │   │       ├── DependInfo.cmake
    │   │   │       ├── flags.make
    │   │   │       ├── link.txt
    │   │   │       ├── progress.make
    │   │   │       ├── test-vad.cpp.o
    │   │   │       └── test-vad.cpp.o.d
    │   │   ├── CTestTestfile.cmake
    │   │   └── Makefile
    │   ├── whisper-config.cmake
    │   ├── whisper-version.cmake
    │   └── whisper.pc
    ├── build-xcframework.sh
    ├── ci
    │   ├── README.md
    │   └── run.sh
    ├── close-issue.yml
    ├── cmake
    │   ├── build-info.cmake
    │   ├── DefaultTargetOptions.cmake
    │   ├── FindFFmpeg.cmake
    │   ├── git-vars.cmake
    │   ├── whisper-config.cmake.in
    │   └── whisper.pc.in
    ├── CMakeLists.txt
    ├── examples
    │   ├── addon.node
    │   │   ├── __test__
    │   │   │   └── whisper.spec.js
    │   │   ├── addon.cpp
    │   │   ├── CMakeLists.txt
    │   │   ├── index.js
    │   │   ├── package.json
    │   │   └── README.md
    │   ├── bench
    │   │   ├── bench.cpp
    │   │   ├── CMakeLists.txt
    │   │   └── README.md
    │   ├── bench.wasm
    │   │   ├── CMakeLists.txt
    │   │   ├── emscripten.cpp
    │   │   ├── index-tmpl.html
    │   │   └── README.md
    │   ├── cli
    │   │   ├── cli.cpp
    │   │   ├── CMakeLists.txt
    │   │   └── README.md
    │   ├── CMakeLists.txt
    │   ├── coi-serviceworker.js
    │   ├── command
    │   │   ├── CMakeLists.txt
    │   │   ├── command.cpp
    │   │   ├── commands.txt
    │   │   └── README.md
    │   ├── command.wasm
    │   │   ├── CMakeLists.txt
    │   │   ├── emscripten.cpp
    │   │   ├── index-tmpl.html
    │   │   └── README.md
    │   ├── common-ggml.cpp
    │   ├── common-ggml.h
    │   ├── common-sdl.cpp
    │   ├── common-sdl.h
    │   ├── common-whisper.cpp
    │   ├── common-whisper.h
    │   ├── common.cpp
    │   ├── common.h
    │   ├── deprecation-warning
    │   │   ├── CMakeLists.txt
    │   │   ├── deprecation-warning.cpp
    │   │   └── README.md
    │   ├── ffmpeg-transcode.cpp
    │   ├── generate-karaoke.sh
    │   ├── grammar-parser.cpp
    │   ├── grammar-parser.h
    │   ├── helpers.js
    │   ├── json.hpp
    │   ├── livestream.sh
    │   ├── lsp
    │   │   ├── CMakeLists.txt
    │   │   ├── lsp.cpp
    │   │   ├── README.md
    │   │   └── whisper.vim
    │   ├── miniaudio.h
    │   ├── python
    │   │   ├── test_whisper_processor.py
    │   │   └── whisper_processor.py
    │   ├── quantize
    │   │   ├── CMakeLists.txt
    │   │   ├── quantize.cpp
    │   │   └── README.md
    │   ├── server
    │   │   ├── CMakeLists.txt
    │   │   ├── httplib.h
    │   │   ├── README.md
    │   │   └── server.cpp
    │   ├── server.py
    │   ├── stb_vorbis.c
    │   ├── stream
    │   │   ├── CMakeLists.txt
    │   │   ├── README.md
    │   │   └── stream.cpp
    │   ├── stream.wasm
    │   │   ├── CMakeLists.txt
    │   │   ├── emscripten.cpp
    │   │   ├── index-tmpl.html
    │   │   └── README.md
    │   ├── sycl
    │   │   ├── build.sh
    │   │   ├── CMakeLists.txt
    │   │   ├── ls-sycl-device.cpp
    │   │   ├── README.md
    │   │   └── run-whisper.sh
    │   ├── talk-llama
    │   │   ├── CMakeLists.txt
    │   │   ├── eleven-labs.py
    │   │   ├── llama-adapter.cpp
    │   │   ├── llama-adapter.h
    │   │   ├── llama-arch.cpp
    │   │   ├── llama-arch.h
    │   │   ├── llama-batch.cpp
    │   │   ├── llama-batch.h
    │   │   ├── llama-chat.cpp
    │   │   ├── llama-chat.h
    │   │   ├── llama-context.cpp
    │   │   ├── llama-context.h
    │   │   ├── llama-cparams.cpp
    │   │   ├── llama-cparams.h
    │   │   ├── llama-grammar.cpp
    │   │   ├── llama-grammar.h
    │   │   ├── llama-graph.cpp
    │   │   ├── llama-graph.h
    │   │   ├── llama-hparams.cpp
    │   │   ├── llama-hparams.h
    │   │   ├── llama-impl.cpp
    │   │   ├── llama-impl.h
    │   │   ├── llama-io.cpp
    │   │   ├── llama-io.h
    │   │   ├── llama-kv-cache.cpp
    │   │   ├── llama-kv-cache.h
    │   │   ├── llama-memory.cpp
    │   │   ├── llama-memory.h
    │   │   ├── llama-mmap.cpp
    │   │   ├── llama-mmap.h
    │   │   ├── llama-model-loader.cpp
    │   │   ├── llama-model-loader.h
    │   │   ├── llama-model-saver.cpp
    │   │   ├── llama-model-saver.h
    │   │   ├── llama-model.cpp
    │   │   ├── llama-model.h
    │   │   ├── llama-quant.cpp
    │   │   ├── llama-quant.h
    │   │   ├── llama-sampling.cpp
    │   │   ├── llama-sampling.h
    │   │   ├── llama-vocab.cpp
    │   │   ├── llama-vocab.h
    │   │   ├── llama.cpp
    │   │   ├── llama.h
    │   │   ├── prompts
    │   │   │   └── talk-alpaca.txt
    │   │   ├── README.md
    │   │   ├── speak
    │   │   ├── speak.bat
    │   │   ├── speak.ps1
    │   │   ├── talk-llama.cpp
    │   │   ├── unicode-data.cpp
    │   │   ├── unicode-data.h
    │   │   ├── unicode.cpp
    │   │   └── unicode.h
    │   ├── twitch.sh
    │   ├── vad-speech-segments
    │   │   ├── CMakeLists.txt
    │   │   ├── README.md
    │   │   └── speech.cpp
    │   ├── wchess
    │   │   ├── CMakeLists.txt
    │   │   ├── libwchess
    │   │   │   ├── Chessboard.cpp
    │   │   │   ├── Chessboard.h
    │   │   │   ├── CMakeLists.txt
    │   │   │   ├── test-chessboard.cpp
    │   │   │   ├── WChess.cpp
    │   │   │   └── WChess.h
    │   │   ├── README.md
    │   │   ├── wchess.cmd
    │   │   │   ├── CMakeLists.txt
    │   │   │   └── wchess.cmd.cpp
    │   │   └── wchess.wasm
    │   │       ├── chessboardjs-1.0.0
    │   │       │   ├── css
    │   │       │   │   ├── chessboard-1.0.0.css
    │   │       │   │   └── chessboard-1.0.0.min.css
    │   │       │   ├── img
    │   │       │   │   └── chesspieces
    │   │       │   │       └── wikipedia
    │   │       │   │           ├── bB.png
    │   │       │   │           ├── bK.png
    │   │       │   │           ├── bN.png
    │   │       │   │           ├── bP.png
    │   │       │   │           ├── bQ.png
    │   │       │   │           ├── bR.png
    │   │       │   │           ├── wB.png
    │   │       │   │           ├── wK.png
    │   │       │   │           ├── wN.png
    │   │       │   │           ├── wP.png
    │   │       │   │           ├── wQ.png
    │   │       │   │           └── wR.png
    │   │       │   └── js
    │   │       │       ├── chessboard-1.0.0
    │   │       │       │   ├── CHANGELOG.md
    │   │       │       │   ├── LICENSE.md
    │   │       │       │   ├── package.json
    │   │       │       │   └── README.md
    │   │       │       ├── chessboard-1.0.0.js
    │   │       │       └── chessboard-1.0.0.min.js
    │   │       ├── CMakeLists.txt
    │   │       ├── index-tmpl.html
    │   │       ├── jquery-3.7.1.min.js
    │   │       └── wchess.wasm.cpp
    │   ├── whisper.android
    │   │   ├── app
    │   │   │   ├── build.gradle
    │   │   │   ├── proguard-rules.pro
    │   │   │   └── src
    │   │   │       ├── androidTest
    │   │   │       │   └── java
    │   │   │       │       └── com
    │   │   │       │           └── whispercppdemo
    │   │   │       │               └── ExampleInstrumentedTest.kt
    │   │   │       ├── main
    │   │   │       │   ├── AndroidManifest.xml
    │   │   │       │   ├── java
    │   │   │       │   │   └── com
    │   │   │       │   │       └── whispercppdemo
    │   │   │       │   │           ├── MainActivity.kt
    │   │   │       │   │           ├── media
    │   │   │       │   │           │   └── RiffWaveHelper.kt
    │   │   │       │   │           ├── recorder
    │   │   │       │   │           │   └── Recorder.kt
    │   │   │       │   │           └── ui
    │   │   │       │   │               ├── main
    │   │   │       │   │               │   ├── MainScreen.kt
    │   │   │       │   │               │   └── MainScreenViewModel.kt
    │   │   │       │   │               └── theme
    │   │   │       │   │                   ├── Color.kt
    │   │   │       │   │                   ├── Theme.kt
    │   │   │       │   │                   └── Type.kt
    │   │   │       │   └── res
    │   │   │       │       ├── drawable
    │   │   │       │       │   ├── ic_launcher_background.xml
    │   │   │       │       │   └── ic_launcher_foreground.xml
    │   │   │       │       ├── mipmap-anydpi
    │   │   │       │       │   └── ic_launcher.xml
    │   │   │       │       ├── values
    │   │   │       │       │   ├── strings.xml
    │   │   │       │       │   └── themes.xml
    │   │   │       │       └── xml
    │   │   │       │           ├── backup_rules.xml
    │   │   │       │           └── data_extraction_rules.xml
    │   │   │       └── test
    │   │   │           └── java
    │   │   │               └── com
    │   │   │                   └── whispercppdemo
    │   │   │                       └── ExampleUnitTest.kt
    │   │   ├── build.gradle
    │   │   ├── gradle
    │   │   │   └── wrapper
    │   │   │       ├── gradle-wrapper.jar
    │   │   │       └── gradle-wrapper.properties
    │   │   ├── gradle.properties
    │   │   ├── gradlew
    │   │   ├── gradlew.bat
    │   │   ├── lib
    │   │   │   ├── build.gradle
    │   │   │   └── src
    │   │   │       └── main
    │   │   │           ├── AndroidManifest.xml
    │   │   │           ├── java
    │   │   │           │   └── com
    │   │   │           │       └── whispercpp
    │   │   │           │           └── whisper
    │   │   │           │               ├── LibWhisper.kt
    │   │   │           │               └── WhisperCpuConfig.kt
    │   │   │           └── jni
    │   │   │               └── whisper
    │   │   │                   ├── CMakeLists.txt
    │   │   │                   └── jni.c
    │   │   ├── README.md
    │   │   └── settings.gradle
    │   ├── whisper.android.java
    │   │   ├── app
    │   │   │   ├── build.gradle
    │   │   │   ├── proguard-rules.pro
    │   │   │   └── src
    │   │   │       ├── androidTest
    │   │   │       │   └── java
    │   │   │       │       └── com
    │   │   │       │           └── litongjava
    │   │   │       │               └── whisper
    │   │   │       │                   └── android
    │   │   │       │                       └── java
    │   │   │       │                           └── ExampleInstrumentedTest.java
    │   │   │       ├── main
    │   │   │       │   ├── AndroidManifest.xml
    │   │   │       │   ├── assets
    │   │   │       │   │   └── logback.xml
    │   │   │       │   ├── java
    │   │   │       │   │   └── com
    │   │   │       │   │       ├── litongjava
    │   │   │       │   │       │   └── whisper
    │   │   │       │   │       │       └── android
    │   │   │       │   │       │           └── java
    │   │   │       │   │       │               ├── app
    │   │   │       │   │       │               │   └── App.java
    │   │   │       │   │       │               ├── bean
    │   │   │       │   │       │               │   └── WhisperSegment.java
    │   │   │       │   │       │               ├── MainActivity.java
    │   │   │       │   │       │               ├── services
    │   │   │       │   │       │               │   └── WhisperService.java
    │   │   │       │   │       │               ├── single
    │   │   │       │   │       │               │   └── LocalWhisper.java
    │   │   │       │   │       │               ├── task
    │   │   │       │   │       │               │   ├── LoadModelTask.java
    │   │   │       │   │       │               │   └── TranscriptionTask.java
    │   │   │       │   │       │               └── utils
    │   │   │       │   │       │                   ├── AssetUtils.java
    │   │   │       │   │       │                   └── WaveEncoder.java
    │   │   │       │   │       └── whispercpp
    │   │   │       │   │           └── java
    │   │   │       │   │               └── whisper
    │   │   │       │   │                   ├── CpuInfo.java
    │   │   │       │   │                   ├── WhisperContext.java
    │   │   │       │   │                   ├── WhisperCpuConfig.java
    │   │   │       │   │                   ├── WhisperLib.java
    │   │   │       │   │                   └── WhisperUtils.java
    │   │   │       │   ├── jni
    │   │   │       │   │   └── whisper
    │   │   │       │   │       ├── CMakeLists.txt
    │   │   │       │   │       └── jni.c
    │   │   │       │   └── res
    │   │   │       │       ├── drawable
    │   │   │       │       │   └── ic_launcher_background.xml
    │   │   │       │       ├── drawable-v24
    │   │   │       │       │   └── ic_launcher_foreground.xml
    │   │   │       │       ├── layout
    │   │   │       │       │   └── activity_main.xml
    │   │   │       │       ├── mipmap-anydpi-v26
    │   │   │       │       │   ├── ic_launcher_round.xml
    │   │   │       │       │   └── ic_launcher.xml
    │   │   │       │       ├── mipmap-hdpi
    │   │   │       │       │   ├── ic_launcher_round.png
    │   │   │       │       │   └── ic_launcher.png
    │   │   │       │       ├── mipmap-mdpi
    │   │   │       │       │   ├── ic_launcher_round.png
    │   │   │       │       │   └── ic_launcher.png
    │   │   │       │       ├── mipmap-xhdpi
    │   │   │       │       │   ├── ic_launcher_round.png
    │   │   │       │       │   └── ic_launcher.png
    │   │   │       │       ├── mipmap-xxhdpi
    │   │   │       │       │   ├── ic_launcher_round.png
    │   │   │       │       │   └── ic_launcher.png
    │   │   │       │       ├── mipmap-xxxhdpi
    │   │   │       │       │   ├── ic_launcher_round.png
    │   │   │       │       │   └── ic_launcher.png
    │   │   │       │       ├── values
    │   │   │       │       │   ├── colors.xml
    │   │   │       │       │   ├── strings.xml
    │   │   │       │       │   └── themes.xml
    │   │   │       │       └── values-night
    │   │   │       │           └── themes.xml
    │   │   │       └── test
    │   │   │           └── java
    │   │   │               └── com
    │   │   │                   └── litongjava
    │   │   │                       └── whisper
    │   │   │                           └── android
    │   │   │                               └── java
    │   │   │                                   └── ExampleUnitTest.java
    │   │   ├── build.gradle
    │   │   ├── gradle
    │   │   │   └── wrapper
    │   │   │       ├── gradle-wrapper.jar
    │   │   │       └── gradle-wrapper.properties
    │   │   ├── gradle.properties
    │   │   ├── gradlew
    │   │   ├── gradlew.bat
    │   │   ├── README_files
    │   │   │   └── 1.jpg
    │   │   ├── README.md
    │   │   └── settings.gradle
    │   ├── whisper.nvim
    │   │   ├── README.md
    │   │   └── whisper.nvim
    │   ├── whisper.objc
    │   │   ├── README.md
    │   │   ├── whisper.objc
    │   │   │   ├── AppDelegate.h
    │   │   │   ├── AppDelegate.m
    │   │   │   ├── Assets.xcassets
    │   │   │   │   ├── AccentColor.colorset
    │   │   │   │   │   └── Contents.json
    │   │   │   │   ├── AppIcon.appiconset
    │   │   │   │   │   └── Contents.json
    │   │   │   │   └── Contents.json
    │   │   │   ├── Base.lproj
    │   │   │   │   ├── LaunchScreen.storyboard
    │   │   │   │   └── Main.storyboard
    │   │   │   ├── Info.plist
    │   │   │   ├── main.m
    │   │   │   ├── SceneDelegate.h
    │   │   │   ├── SceneDelegate.m
    │   │   │   ├── ViewController.h
    │   │   │   └── ViewController.m
    │   │   └── whisper.objc.xcodeproj
    │   │       ├── project.pbxproj
    │   │       └── project.xcworkspace
    │   │           ├── contents.xcworkspacedata
    │   │           └── xcshareddata
    │   │               └── IDEWorkspaceChecks.plist
    │   ├── whisper.swiftui
    │   │   ├── README.md
    │   │   ├── whisper.cpp.swift
    │   │   │   └── LibWhisper.swift
    │   │   ├── whisper.swiftui.demo
    │   │   │   ├── Models
    │   │   │   │   ├── Model.swift
    │   │   │   │   └── WhisperState.swift
    │   │   │   ├── Resources
    │   │   │   │   ├── models
    │   │   │   │   └── samples
    │   │   │   ├── Supporting files
    │   │   │   │   ├── Assets.xcassets
    │   │   │   │   │   ├── AccentColor.colorset
    │   │   │   │   │   │   └── Contents.json
    │   │   │   │   │   ├── AppIcon.appiconset
    │   │   │   │   │   │   └── Contents.json
    │   │   │   │   │   └── Contents.json
    │   │   │   │   ├── Preview Content
    │   │   │   │   │   └── Preview Assets.xcassets
    │   │   │   │   │       └── Contents.json
    │   │   │   │   └── WhisperCppDemo.entitlements
    │   │   │   ├── UI
    │   │   │   │   ├── ContentView.swift
    │   │   │   │   └── DownloadButton.swift
    │   │   │   ├── Utils
    │   │   │   │   ├── Recorder.swift
    │   │   │   │   └── RiffWaveUtils.swift
    │   │   │   └── WhisperCppDemoApp.swift
    │   │   └── whisper.swiftui.xcodeproj
    │   │       ├── project.pbxproj
    │   │       ├── project.xcworkspace
    │   │       │   └── xcshareddata
    │   │       │       └── IDEWorkspaceChecks.plist
    │   │       └── xcshareddata
    │   │           └── xcschemes
    │   │               └── WhisperCppDemo.xcscheme
    │   ├── whisper.wasm
    │   │   ├── CMakeLists.txt
    │   │   ├── emscripten.cpp
    │   │   ├── index-tmpl.html
    │   │   └── README.md
    │   └── yt-wsp.sh
    ├── ggml
    │   ├── cmake
    │   │   ├── BuildTypes.cmake
    │   │   ├── common.cmake
    │   │   ├── ggml-config.cmake.in
    │   │   └── GitVars.cmake
    │   ├── CMakeLists.txt
    │   ├── include
    │   │   ├── ggml-alloc.h
    │   │   ├── ggml-backend.h
    │   │   ├── ggml-blas.h
    │   │   ├── ggml-cann.h
    │   │   ├── ggml-cpp.h
    │   │   ├── ggml-cpu.h
    │   │   ├── ggml-cuda.h
    │   │   ├── ggml-kompute.h
    │   │   ├── ggml-metal.h
    │   │   ├── ggml-opencl.h
    │   │   ├── ggml-opt.h
    │   │   ├── ggml-rpc.h
    │   │   ├── ggml-sycl.h
    │   │   ├── ggml-vulkan.h
    │   │   ├── ggml.h
    │   │   └── gguf.h
    │   └── src
    │       ├── CMakeLists.txt
    │       ├── ggml-alloc.c
    │       ├── ggml-amx
    │       │   ├── CMakeLists.txt
    │       │   ├── common.h
    │       │   ├── ggml-amx.cpp
    │       │   ├── mmq.cpp
    │       │   └── mmq.h
    │       ├── ggml-backend-impl.h
    │       ├── ggml-backend-reg.cpp
    │       ├── ggml-backend.cpp
    │       ├── ggml-blas
    │       │   ├── CMakeLists.txt
    │       │   └── ggml-blas.cpp
    │       ├── ggml-cann
    │       │   ├── acl_tensor.cpp
    │       │   ├── acl_tensor.h
    │       │   ├── aclnn_ops.cpp
    │       │   ├── aclnn_ops.h
    │       │   ├── CMakeLists.txt
    │       │   ├── common.h
    │       │   ├── Doxyfile
    │       │   ├── ggml-cann.cpp
    │       │   └── kernels
    │       │       ├── ascendc_kernels.h
    │       │       ├── CMakeLists.txt
    │       │       ├── dup.cpp
    │       │       ├── get_row_f16.cpp
    │       │       ├── get_row_f32.cpp
    │       │       ├── get_row_q4_0.cpp
    │       │       ├── get_row_q8_0.cpp
    │       │       ├── quantize_f16_q8_0.cpp
    │       │       ├── quantize_f32_q8_0.cpp
    │       │       └── quantize_float_to_q4_0.cpp
    │       ├── ggml-common.h
    │       ├── ggml-cpu
    │       │   ├── amx
    │       │   │   ├── amx.cpp
    │       │   │   ├── amx.h
    │       │   │   ├── common.h
    │       │   │   ├── mmq.cpp
    │       │   │   └── mmq.h
    │       │   ├── binary-ops.cpp
    │       │   ├── binary-ops.h
    │       │   ├── cmake
    │       │   │   └── FindSIMD.cmake
    │       │   ├── CMakeLists.txt
    │       │   ├── common.h
    │       │   ├── cpu-feats-x86.cpp
    │       │   ├── ggml-cpu-aarch64.cpp
    │       │   ├── ggml-cpu-aarch64.h
    │       │   ├── ggml-cpu-hbm.cpp
    │       │   ├── ggml-cpu-hbm.h
    │       │   ├── ggml-cpu-impl.h
    │       │   ├── ggml-cpu-quants.c
    │       │   ├── ggml-cpu-quants.h
    │       │   ├── ggml-cpu-traits.cpp
    │       │   ├── ggml-cpu-traits.h
    │       │   ├── ggml-cpu.c
    │       │   ├── ggml-cpu.cpp
    │       │   ├── kleidiai
    │       │   │   ├── kernels.cpp
    │       │   │   ├── kernels.h
    │       │   │   ├── kleidiai.cpp
    │       │   │   └── kleidiai.h
    │       │   ├── llamafile
    │       │   │   ├── sgemm.cpp
    │       │   │   └── sgemm.h
    │       │   ├── ops.cpp
    │       │   ├── ops.h
    │       │   ├── simd-mappings.h
    │       │   ├── unary-ops.cpp
    │       │   ├── unary-ops.h
    │       │   ├── vec.cpp
    │       │   └── vec.h
    │       ├── ggml-cuda
    │       │   ├── acc.cu
    │       │   ├── acc.cuh
    │       │   ├── arange.cu
    │       │   ├── arange.cuh
    │       │   ├── argmax.cu
    │       │   ├── argmax.cuh
    │       │   ├── argsort.cu
    │       │   ├── argsort.cuh
    │       │   ├── binbcast.cu
    │       │   ├── binbcast.cuh
    │       │   ├── clamp.cu
    │       │   ├── clamp.cuh
    │       │   ├── CMakeLists.txt
    │       │   ├── common.cuh
    │       │   ├── concat.cu
    │       │   ├── concat.cuh
    │       │   ├── conv-transpose-1d.cu
    │       │   ├── conv-transpose-1d.cuh
    │       │   ├── convert.cu
    │       │   ├── convert.cuh
    │       │   ├── count-equal.cu
    │       │   ├── count-equal.cuh
    │       │   ├── cp-async.cuh
    │       │   ├── cpy.cu
    │       │   ├── cpy.cuh
    │       │   ├── cross-entropy-loss.cu
    │       │   ├── cross-entropy-loss.cuh
    │       │   ├── dequantize.cuh
    │       │   ├── diagmask.cu
    │       │   ├── diagmask.cuh
    │       │   ├── fattn-common.cuh
    │       │   ├── fattn-mma-f16.cuh
    │       │   ├── fattn-tile-f16.cu
    │       │   ├── fattn-tile-f16.cuh
    │       │   ├── fattn-tile-f32.cu
    │       │   ├── fattn-tile-f32.cuh
    │       │   ├── fattn-vec-f16.cuh
    │       │   ├── fattn-vec-f32.cuh
    │       │   ├── fattn-wmma-f16.cu
    │       │   ├── fattn-wmma-f16.cuh
    │       │   ├── fattn.cu
    │       │   ├── fattn.cuh
    │       │   ├── getrows.cu
    │       │   ├── getrows.cuh
    │       │   ├── ggml-cuda.cu
    │       │   ├── gla.cu
    │       │   ├── gla.cuh
    │       │   ├── im2col.cu
    │       │   ├── im2col.cuh
    │       │   ├── mma.cuh
    │       │   ├── mmq.cu
    │       │   ├── mmq.cuh
    │       │   ├── mmv.cu
    │       │   ├── mmv.cuh
    │       │   ├── mmvq.cu
    │       │   ├── mmvq.cuh
    │       │   ├── norm.cu
    │       │   ├── norm.cuh
    │       │   ├── opt-step-adamw.cu
    │       │   ├── opt-step-adamw.cuh
    │       │   ├── out-prod.cu
    │       │   ├── out-prod.cuh
    │       │   ├── pad.cu
    │       │   ├── pad.cuh
    │       │   ├── pool2d.cu
    │       │   ├── pool2d.cuh
    │       │   ├── quantize.cu
    │       │   ├── quantize.cuh
    │       │   ├── rope.cu
    │       │   ├── rope.cuh
    │       │   ├── scale.cu
    │       │   ├── scale.cuh
    │       │   ├── softmax.cu
    │       │   ├── softmax.cuh
    │       │   ├── ssm-conv.cu
    │       │   ├── ssm-conv.cuh
    │       │   ├── ssm-scan.cu
    │       │   ├── ssm-scan.cuh
    │       │   ├── sum.cu
    │       │   ├── sum.cuh
    │       │   ├── sumrows.cu
    │       │   ├── sumrows.cuh
    │       │   ├── template-instances
    │       │   │   ├── fattn-mma-f16-instance-ncols1_1-ncols2_16.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_1-ncols2_8.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_16-ncols2_1.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_16-ncols2_2.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_16-ncols2_4.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_2-ncols2_16.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_2-ncols2_4.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_2-ncols2_8.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_32-ncols2_1.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_32-ncols2_2.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_4-ncols2_16.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_4-ncols2_2.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_4-ncols2_4.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_4-ncols2_8.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_64-ncols2_1.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_8-ncols2_1.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_8-ncols2_2.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_8-ncols2_4.cu
    │       │   │   ├── fattn-mma-f16-instance-ncols1_8-ncols2_8.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-f16-f16.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-f16-q4_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-f16-q4_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-f16-q5_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-f16-q5_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-f16-q8_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q4_0-f16.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q4_0-q4_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q4_0-q4_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q4_0-q5_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q4_0-q5_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q4_0-q8_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q4_1-f16.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q4_1-q4_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q4_1-q4_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q4_1-q5_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q4_1-q5_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q4_1-q8_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q5_0-f16.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q5_0-q4_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q5_0-q4_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q5_0-q5_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q5_0-q5_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q5_0-q8_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q5_1-f16.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q5_1-q4_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q5_1-q4_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q5_1-q5_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q5_1-q5_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q5_1-q8_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q8_0-f16.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q8_0-q4_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q8_0-q4_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q8_0-q5_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q8_0-q5_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs128-q8_0-q8_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs256-f16-f16.cu
    │       │   │   ├── fattn-vec-f16-instance-hs64-f16-f16.cu
    │       │   │   ├── fattn-vec-f16-instance-hs64-f16-q4_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs64-f16-q4_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs64-f16-q5_0.cu
    │       │   │   ├── fattn-vec-f16-instance-hs64-f16-q5_1.cu
    │       │   │   ├── fattn-vec-f16-instance-hs64-f16-q8_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-f16-f16.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-f16-q4_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-f16-q4_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-f16-q5_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-f16-q5_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-f16-q8_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q4_0-f16.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q4_0-q4_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q4_0-q4_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q4_0-q5_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q4_0-q5_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q4_0-q8_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q4_1-f16.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q4_1-q4_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q4_1-q4_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q4_1-q5_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q4_1-q5_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q4_1-q8_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q5_0-f16.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q5_0-q4_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q5_0-q4_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q5_0-q5_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q5_0-q5_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q5_0-q8_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q5_1-f16.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q5_1-q4_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q5_1-q4_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q5_1-q5_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q5_1-q5_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q5_1-q8_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q8_0-f16.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q8_0-q4_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q8_0-q4_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q8_0-q5_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q8_0-q5_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs128-q8_0-q8_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs256-f16-f16.cu
    │       │   │   ├── fattn-vec-f32-instance-hs64-f16-f16.cu
    │       │   │   ├── fattn-vec-f32-instance-hs64-f16-q4_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs64-f16-q4_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs64-f16-q5_0.cu
    │       │   │   ├── fattn-vec-f32-instance-hs64-f16-q5_1.cu
    │       │   │   ├── fattn-vec-f32-instance-hs64-f16-q8_0.cu
    │       │   │   ├── generate_cu_files.py
    │       │   │   ├── mmq-instance-iq1_s.cu
    │       │   │   ├── mmq-instance-iq2_s.cu
    │       │   │   ├── mmq-instance-iq2_xs.cu
    │       │   │   ├── mmq-instance-iq2_xxs.cu
    │       │   │   ├── mmq-instance-iq3_s.cu
    │       │   │   ├── mmq-instance-iq3_xxs.cu
    │       │   │   ├── mmq-instance-iq4_nl.cu
    │       │   │   ├── mmq-instance-iq4_xs.cu
    │       │   │   ├── mmq-instance-q2_k.cu
    │       │   │   ├── mmq-instance-q3_k.cu
    │       │   │   ├── mmq-instance-q4_0.cu
    │       │   │   ├── mmq-instance-q4_1.cu
    │       │   │   ├── mmq-instance-q4_k.cu
    │       │   │   ├── mmq-instance-q5_0.cu
    │       │   │   ├── mmq-instance-q5_1.cu
    │       │   │   ├── mmq-instance-q5_k.cu
    │       │   │   ├── mmq-instance-q6_k.cu
    │       │   │   └── mmq-instance-q8_0.cu
    │       │   ├── tsembd.cu
    │       │   ├── tsembd.cuh
    │       │   ├── unary.cu
    │       │   ├── unary.cuh
    │       │   ├── upscale.cu
    │       │   ├── upscale.cuh
    │       │   ├── vecdotq.cuh
    │       │   ├── vendors
    │       │   │   ├── cuda.h
    │       │   │   ├── hip.h
    │       │   │   └── musa.h
    │       │   ├── wkv.cu
    │       │   └── wkv.cuh
    │       ├── ggml-hip
    │       │   └── CMakeLists.txt
    │       ├── ggml-impl.h
    │       ├── ggml-kompute
    │       │   ├── CMakeLists.txt
    │       │   ├── ggml-kompute.cpp
    │       │   └── kompute-shaders
    │       │       ├── common.comp
    │       │       ├── op_add.comp
    │       │       ├── op_addrow.comp
    │       │       ├── op_cpy_f16_f16.comp
    │       │       ├── op_cpy_f16_f32.comp
    │       │       ├── op_cpy_f32_f16.comp
    │       │       ├── op_cpy_f32_f32.comp
    │       │       ├── op_diagmask.comp
    │       │       ├── op_gelu.comp
    │       │       ├── op_getrows_f16.comp
    │       │       ├── op_getrows_f32.comp
    │       │       ├── op_getrows_q4_0.comp
    │       │       ├── op_getrows_q4_1.comp
    │       │       ├── op_getrows_q6_k.comp
    │       │       ├── op_getrows.comp
    │       │       ├── op_mul_mat_f16.comp
    │       │       ├── op_mul_mat_mat_f32.comp
    │       │       ├── op_mul_mat_q4_0.comp
    │       │       ├── op_mul_mat_q4_1.comp
    │       │       ├── op_mul_mat_q4_k.comp
    │       │       ├── op_mul_mat_q6_k.comp
    │       │       ├── op_mul_mat_q8_0.comp
    │       │       ├── op_mul_mv_q_n_pre.comp
    │       │       ├── op_mul_mv_q_n.comp
    │       │       ├── op_mul.comp
    │       │       ├── op_norm.comp
    │       │       ├── op_relu.comp
    │       │       ├── op_rmsnorm.comp
    │       │       ├── op_rope_neox_f16.comp
    │       │       ├── op_rope_neox_f32.comp
    │       │       ├── op_rope_norm_f16.comp
    │       │       ├── op_rope_norm_f32.comp
    │       │       ├── op_scale_8.comp
    │       │       ├── op_scale.comp
    │       │       ├── op_silu.comp
    │       │       ├── op_softmax.comp
    │       │       └── rope_common.comp
    │       ├── ggml-metal
    │       │   ├── CMakeLists.txt
    │       │   ├── ggml-metal-impl.h
    │       │   ├── ggml-metal.m
    │       │   └── ggml-metal.metal
    │       ├── ggml-musa
    │       │   └── CMakeLists.txt
    │       ├── ggml-opencl
    │       │   ├── CMakeLists.txt
    │       │   ├── ggml-opencl.cpp
    │       │   └── kernels
    │       │       ├── add.cl
    │       │       ├── clamp.cl
    │       │       ├── cpy.cl
    │       │       ├── cvt.cl
    │       │       ├── diag_mask_inf.cl
    │       │       ├── embed_kernel.py
    │       │       ├── gelu.cl
    │       │       ├── gemv_noshuffle_general.cl
    │       │       ├── gemv_noshuffle.cl
    │       │       ├── get_rows.cl
    │       │       ├── im2col_f16.cl
    │       │       ├── im2col_f32.cl
    │       │       ├── mul_mat_Ab_Bi_8x4.cl
    │       │       ├── mul_mv_f16_f16.cl
    │       │       ├── mul_mv_f16_f32_1row.cl
    │       │       ├── mul_mv_f16_f32_l4.cl
    │       │       ├── mul_mv_f16_f32.cl
    │       │       ├── mul_mv_f32_f32.cl
    │       │       ├── mul_mv_q4_0_f32_1d_16x_flat.cl
    │       │       ├── mul_mv_q4_0_f32_1d_8x_flat.cl
    │       │       ├── mul_mv_q4_0_f32_8x_flat.cl
    │       │       ├── mul_mv_q4_0_f32_v.cl
    │       │       ├── mul_mv_q4_0_f32.cl
    │       │       ├── mul_mv_q6_k.cl
    │       │       ├── mul.cl
    │       │       ├── norm.cl
    │       │       ├── relu.cl
    │       │       ├── rms_norm.cl
    │       │       ├── rope.cl
    │       │       ├── scale.cl
    │       │       ├── silu.cl
    │       │       ├── softmax_4_f16.cl
    │       │       ├── softmax_4_f32.cl
    │       │       ├── softmax_f16.cl
    │       │       ├── softmax_f32.cl
    │       │       └── transpose.cl
    │       ├── ggml-opt.cpp
    │       ├── ggml-quants.c
    │       ├── ggml-quants.h
    │       ├── ggml-rpc
    │       │   ├── CMakeLists.txt
    │       │   └── ggml-rpc.cpp
    │       ├── ggml-sycl
    │       │   ├── backend.hpp
    │       │   ├── binbcast.cpp
    │       │   ├── binbcast.hpp
    │       │   ├── CMakeLists.txt
    │       │   ├── common.cpp
    │       │   ├── common.hpp
    │       │   ├── concat.cpp
    │       │   ├── concat.hpp
    │       │   ├── conv.cpp
    │       │   ├── conv.hpp
    │       │   ├── convert.cpp
    │       │   ├── convert.hpp
    │       │   ├── cpy.cpp
    │       │   ├── cpy.hpp
    │       │   ├── dequantize.hpp
    │       │   ├── dmmv.cpp
    │       │   ├── dmmv.hpp
    │       │   ├── dpct
    │       │   │   └── helper.hpp
    │       │   ├── element_wise.cpp
    │       │   ├── element_wise.hpp
    │       │   ├── gemm.hpp
    │       │   ├── getrows.cpp
    │       │   ├── getrows.hpp
    │       │   ├── ggml-sycl.cpp
    │       │   ├── gla.cpp
    │       │   ├── gla.hpp
    │       │   ├── im2col.cpp
    │       │   ├── im2col.hpp
    │       │   ├── mmq.cpp
    │       │   ├── mmq.hpp
    │       │   ├── mmvq.cpp
    │       │   ├── mmvq.hpp
    │       │   ├── norm.cpp
    │       │   ├── norm.hpp
    │       │   ├── outprod.cpp
    │       │   ├── outprod.hpp
    │       │   ├── presets.hpp
    │       │   ├── quants.hpp
    │       │   ├── rope.cpp
    │       │   ├── rope.hpp
    │       │   ├── softmax.cpp
    │       │   ├── softmax.hpp
    │       │   ├── sycl_hw.cpp
    │       │   ├── sycl_hw.hpp
    │       │   ├── tsembd.cpp
    │       │   ├── tsembd.hpp
    │       │   ├── vecdotq.hpp
    │       │   ├── wkv.cpp
    │       │   └── wkv.hpp
    │       ├── ggml-threading.cpp
    │       ├── ggml-threading.h
    │       ├── ggml-vulkan
    │       │   ├── cmake
    │       │   │   └── host-toolchain.cmake.in
    │       │   ├── CMakeLists.txt
    │       │   ├── ggml-vulkan.cpp
    │       │   └── vulkan-shaders
    │       │       ├── acc.comp
    │       │       ├── add.comp
    │       │       ├── argmax.comp
    │       │       ├── argsort.comp
    │       │       ├── clamp.comp
    │       │       ├── CMakeLists.txt
    │       │       ├── concat.comp
    │       │       ├── contig_copy.comp
    │       │       ├── conv2d_dw.comp
    │       │       ├── copy_from_quant.comp
    │       │       ├── copy_to_quant.comp
    │       │       ├── copy.comp
    │       │       ├── cos.comp
    │       │       ├── count_equal.comp
    │       │       ├── dequant_f32.comp
    │       │       ├── dequant_funcs_cm2.comp
    │       │       ├── dequant_funcs.comp
    │       │       ├── dequant_head.comp
    │       │       ├── dequant_iq1_m.comp
    │       │       ├── dequant_iq1_s.comp
    │       │       ├── dequant_iq2_s.comp
    │       │       ├── dequant_iq2_xs.comp
    │       │       ├── dequant_iq2_xxs.comp
    │       │       ├── dequant_iq3_s.comp
    │       │       ├── dequant_iq3_xxs.comp
    │       │       ├── dequant_iq4_nl.comp
    │       │       ├── dequant_iq4_xs.comp
    │       │       ├── dequant_q2_k.comp
    │       │       ├── dequant_q3_k.comp
    │       │       ├── dequant_q4_0.comp
    │       │       ├── dequant_q4_1.comp
    │       │       ├── dequant_q4_k.comp
    │       │       ├── dequant_q5_0.comp
    │       │       ├── dequant_q5_1.comp
    │       │       ├── dequant_q5_k.comp
    │       │       ├── dequant_q6_k.comp
    │       │       ├── dequant_q8_0.comp
    │       │       ├── diag_mask_inf.comp
    │       │       ├── div.comp
    │       │       ├── flash_attn_cm2.comp
    │       │       ├── flash_attn_split_k_reduce.comp
    │       │       ├── flash_attn.comp
    │       │       ├── gelu_quick.comp
    │       │       ├── gelu.comp
    │       │       ├── generic_binary_head.comp
    │       │       ├── generic_head.comp
    │       │       ├── generic_unary_head.comp
    │       │       ├── get_rows_quant.comp
    │       │       ├── get_rows.comp
    │       │       ├── group_norm.comp
    │       │       ├── im2col.comp
    │       │       ├── l2_norm.comp
    │       │       ├── leaky_relu.comp
    │       │       ├── mul_mat_split_k_reduce.comp
    │       │       ├── mul_mat_vec_base.comp
    │       │       ├── mul_mat_vec_iq1_m.comp
    │       │       ├── mul_mat_vec_iq1_s.comp
    │       │       ├── mul_mat_vec_iq2_s.comp
    │       │       ├── mul_mat_vec_iq2_xs.comp
    │       │       ├── mul_mat_vec_iq2_xxs.comp
    │       │       ├── mul_mat_vec_iq3_s.comp
    │       │       ├── mul_mat_vec_iq3_xxs.comp
    │       │       ├── mul_mat_vec_nc.comp
    │       │       ├── mul_mat_vec_p021.comp
    │       │       ├── mul_mat_vec_q2_k.comp
    │       │       ├── mul_mat_vec_q3_k.comp
    │       │       ├── mul_mat_vec_q4_k.comp
    │       │       ├── mul_mat_vec_q5_k.comp
    │       │       ├── mul_mat_vec_q6_k.comp
    │       │       ├── mul_mat_vec.comp
    │       │       ├── mul_mm_cm2.comp
    │       │       ├── mul_mm.comp
    │       │       ├── mul_mmq_funcs.comp
    │       │       ├── mul_mmq.comp
    │       │       ├── mul.comp
    │       │       ├── norm.comp
    │       │       ├── opt_step_adamw.comp
    │       │       ├── pad.comp
    │       │       ├── pool2d.comp
    │       │       ├── quantize_q8_1.comp
    │       │       ├── relu.comp
    │       │       ├── repeat_back.comp
    │       │       ├── repeat.comp
    │       │       ├── rms_norm_back.comp
    │       │       ├── rms_norm.comp
    │       │       ├── rope_head.comp
    │       │       ├── rope_multi.comp
    │       │       ├── rope_neox.comp
    │       │       ├── rope_norm.comp
    │       │       ├── rope_vision.comp
    │       │       ├── scale.comp
    │       │       ├── sigmoid.comp
    │       │       ├── silu_back.comp
    │       │       ├── silu.comp
    │       │       ├── sin.comp
    │       │       ├── soft_max_back.comp
    │       │       ├── soft_max.comp
    │       │       ├── square.comp
    │       │       ├── sub.comp
    │       │       ├── sum_rows.comp
    │       │       ├── tanh.comp
    │       │       ├── test_bfloat16_support.comp
    │       │       ├── test_coopmat_support.comp
    │       │       ├── test_coopmat2_support.comp
    │       │       ├── test_integer_dot_support.comp
    │       │       ├── timestep_embedding.comp
    │       │       ├── types.comp
    │       │       ├── upscale.comp
    │       │       ├── vulkan-shaders-gen.cpp
    │       │       ├── wkv6.comp
    │       │       └── wkv7.comp
    │       ├── ggml.c
    │       └── gguf.cpp
    ├── grammars
    │   ├── assistant.gbnf
    │   ├── chess.gbnf
    │   └── colors.gbnf
    ├── include
    │   └── whisper.h
    ├── LICENSE
    ├── Makefile
    ├── models
    │   ├── convert-h5-to-coreml.py
    │   ├── convert-h5-to-ggml.py
    │   ├── convert-pt-to-ggml.py
    │   ├── convert-silero-vad-to-ggml.py
    │   ├── convert-whisper-to-coreml.py
    │   ├── convert-whisper-to-openvino.py
    │   ├── download-coreml-model.sh
    │   ├── download-ggml-model.cmd
    │   ├── download-ggml-model.sh
    │   ├── download-vad-model.cmd
    │   ├── download-vad-model.sh
    │   ├── for-tests-ggml-base.bin
    │   ├── for-tests-ggml-base.en.bin
    │   ├── for-tests-ggml-large.bin
    │   ├── for-tests-ggml-medium.bin
    │   ├── for-tests-ggml-medium.en.bin
    │   ├── for-tests-ggml-small.bin
    │   ├── for-tests-ggml-small.en.bin
    │   ├── for-tests-ggml-tiny.bin
    │   ├── for-tests-ggml-tiny.en.bin
    │   ├── for-tests-silero-v5.1.2-ggml.bin
    │   ├── generate-coreml-interface.sh
    │   ├── generate-coreml-model.sh
    │   ├── ggml_to_pt.py
    │   ├── ggml-medium.bin
    │   ├── README.md
    │   ├── requirements-coreml.txt
    │   └── requirements-openvino.txt
    ├── README_sycl.md
    ├── README.md
    ├── samples
    │   ├── jfk.mp3
    │   ├── jfk.wav
    │   └── README.md
    ├── scripts
    │   ├── apple
    │   │   ├── validate-apps.sh
    │   │   ├── validate-ios.sh
    │   │   ├── validate-macos.sh
    │   │   ├── validate-tvos.sh
    │   │   └── validate-visionos.sh
    │   ├── bench-all-gg.txt
    │   ├── bench-all.sh
    │   ├── bench-wts.sh
    │   ├── bench.py
    │   ├── build-info.sh
    │   ├── convert-all.sh
    │   ├── deploy-wasm.sh
    │   ├── gen-authors.sh
    │   ├── get-flags.mk
    │   ├── quantize-all.sh
    │   ├── sha-all.sh
    │   ├── sync-ggml-am.sh
    │   ├── sync-ggml.last
    │   ├── sync-ggml.sh
    │   └── sync-llama.sh
    ├── src
    │   ├── CMakeLists.txt
    │   ├── coreml
    │   │   ├── whisper-decoder-impl.h
    │   │   ├── whisper-decoder-impl.m
    │   │   ├── whisper-encoder-impl.h
    │   │   ├── whisper-encoder-impl.m
    │   │   ├── whisper-encoder.h
    │   │   └── whisper-encoder.mm
    │   ├── openvino
    │   │   ├── whisper-openvino-encoder.cpp
    │   │   └── whisper-openvino-encoder.h
    │   ├── whisper-arch.h
    │   └── whisper.cpp
    └── tests
        ├── CMakeLists.txt
        ├── en-0-ref.txt
        ├── en-1-ref.txt
        ├── en-2-ref.txt
        ├── es-0-ref.txt
        ├── librispeech
        │   ├── eval.mk
        │   ├── eval.py
        │   ├── Makefile
        │   ├── normalizers
        │   │   ├── __init__.py
        │   │   ├── basic.py
        │   │   ├── english.json
        │   │   ├── english.py
        │   │   └── LICENSE
        │   ├── README.md
        │   └── requirements.txt
        ├── run-tests.sh
        ├── test-c.c
        ├── test-vad-full.cpp
        ├── test-vad.cpp
        └── test-whisper.js

335 directories, 1695 files
