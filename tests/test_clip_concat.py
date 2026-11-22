import pytest
import media.clip_concat as mod

CASES = [
    ("unified_timebase", (1, 2)),
    ("fps_convert", (30, 24)),
    ("audio_align", (0.5, 0.2)),
    ("gop_align", (2.0, 30)),
    ("pad_black", (0.5, 1.0)),
    ("subtitle_shift", (10.0, 5.0)),
    ("metadata_merge", (1, 2)),
    ("cover_pick", (1, 2)),
    ("duration_dedup", (10.0, 9.5)),
    ("chapter_recalc", (1, 2)),
    ("timecode_offset", (1, 2)),
    ("stream_copy", (1, 2)),
    ("keyframe_force", (1, 2)),
    ("concat_demux", (1, 2)),
    ("duration_sum", ([10.0, 20.0],)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
