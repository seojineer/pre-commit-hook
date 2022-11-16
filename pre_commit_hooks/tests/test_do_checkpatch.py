import pytest
import os
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader 

curr_path = os.path.dirname(os.path.realpath(__file__))
spec = spec_from_loader("do-checkpatch", SourceFileLoader("do-checkpatch", f"{curr_path}/../do-checkpatch"))
do_checkpatch = module_from_spec(spec)
spec.loader.exec_module(do_checkpatch)


@pytest.fixture
def checkpatch_error_result():
    return """ERROR: do not initialise globals to 0
#7: FILE: pre_commit_hooks/test.c:1:
+int a = 0;

total: 1 errors, 0 warnings, 0 checks, 1 lines checked

NOTE: For some of the reported defects, checkpatch may be able to
      mechanically convert to the typical style using --fix or --fix-inplace.

Your patch has style problems, please review.

NOTE: Ignored message types: C99_COMMENTS COMPLEX_MACRO CONST_READ_MOSTLY CORRUPTED_PATCH DEFINE_ARCH_HAS DIFF_IN_COMMIT_MSG FILE_PATH_CHANGES GERRIT_CHANGE_ID GIT_COMMIT_ID IF_0 INIT_ATTRIBUTE LOCKDEP MISSING_SIGN_OFF MODIFIED_INCLUDE_ASM NON_OCTAL_PERMISSIONS NO_AUTHOR_SIGN_OFF SPDX_LICENSE_TAG TEST_ATTR TEST_NOT_ATTR TEST_NOT_TYPE TEST_TYPE UAPI_INCLUDE WEAK_DECLARATION

NOTE: If any of the errors are false positives, please report
      them to the maintainer, see CHECKPATCH in MAINTAINERS.

    """

@pytest.fixture
def checkpatch_warn_result():
    return """WARNING: 'excludind' may be misspelled - perhaps 'excluding'?
#75: FILE: pre_commit_hooks/pcie-isr-fifo.c:69:
+			uint32_t mask = 0xF8C0FFFF; // excludind LTSSM and LINK SPEED
 			                               ^^^^^^^^^

CHECK: Prefer kernel type 'u32' over 'uint32_t'
#75: FILE: pre_commit_hooks/pcie-isr-fifo.c:69:
+			uint32_t mask = 0xF8C0FFFF; // excludind LTSSM and LINK SPEED

WARNING: line length of 103 exceeds 100 columns
#78: FILE: pre_commit_hooks/pcie-isr-fifo.c:72:
+	printf("%16" PRIx64 " %c%02d P%x %-20s(%08" PRIx32 "): ", timer_us(0), CPUPREFIX, get_pcpuid(),

CHECK: Avoid CamelCase: <PRIx64>
#78: FILE: pre_commit_hooks/pcie-isr-fifo.c:72:
+	printf("%16" PRIx64 " %c%02d P%x %-20s(%08" PRIx32 "): ", timer_us(0), CPUPREFIX, get_pcpuid(),

CHECK: Avoid CamelCase: <PRIx32>
#78: FILE: pre_commit_hooks/pcie-isr-fifo.c:72:
+	printf("%16" PRIx64 " %c%02d P%x %-20s(%08" PRIx32 "): ", timer_us(0), CPUPREFIX, get_pcpuid(),

CHECK: Alignment should match open parenthesis
#79: FILE: pre_commit_hooks/pcie-isr-fifo.c:73:
+	printf("%16" PRIx64 " %c%02d P%x %-20s(%08" PRIx32 "): ", timer_us(0), CPUPREFIX, get_pcpuid(),
+			portnum, "EVENT LOG", status);

WARNING: Missing a blank line after declarations
#83: FILE: pre_commit_hooks/pcie-isr-fifo.c:77:
+		int offset = __builtin_ctz(status);
+		printf("%s ", str_pcie_event[offset]);

total: 0 errors, 3 warnings, 4 checks, 81 lines checked

NOTE: For some of the reported defects, checkpatch may be able to
      mechanically convert to the typical style using --fix or --fix-inplace.

Your patch has style problems, please review.

NOTE: Ignored message types: C99_COMMENTS COMPLEX_MACRO CONST_READ_MOSTLY CORRUPTED_PATCH DEFINE_ARCH_HAS DIFF_IN_COMMIT_MSG FILE_PATH_CHANGES GERRIT_CHANGE_ID GIT_COMMIT_ID IF_0 INIT_ATTRIBUTE LOCKDEP MISSING_SIGN_OFF MODIFIED_INCLUDE_ASM NON_OCTAL_PERMISSIONS NO_AUTHOR_SIGN_OFF SPDX_LICENSE_TAG TEST_ATTR TEST_NOT_ATTR TEST_NOT_TYPE TEST_TYPE UAPI_INCLUDE WEAK_DECLARATION

NOTE: If any of the errors are false positives, please report
      them to the maintainer, see CHECKPATCH in MAINTAINERS.
    """

def test_check_result_with_error(checkpatch_error_result):
    with pytest.raises(Exception):
        do_checkpatch.check_result(checkpatch_error_result)

def test_check_result_with_warn(checkpatch_warn_result):
    try:
        do_checkpatch.check_result(checkpatch_warn_result)
    except Exception:
        pytest.fail("When only warnin exist, it should be Pass.")
