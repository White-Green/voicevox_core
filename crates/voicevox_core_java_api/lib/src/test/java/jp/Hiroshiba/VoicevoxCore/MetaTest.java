/*
 * This Java source file was generated by the Gradle 'init' task.
 */
package jp.Hiroshiba.VoicevoxCore;

import org.junit.jupiter.api.Test;

import java.io.File;

class MetaTest {
  @Test
  void checkLoad() {
    // cwdはvoicevox_core/crates/voicevox_core_java_api/lib
    String cwd = System.getProperty("user.dir");
    File path = new File(
        cwd + "/../../../model/sample.vvm");
    try (VoiceModel model = new VoiceModel(path.getAbsolutePath())) {
    }
  }
}
