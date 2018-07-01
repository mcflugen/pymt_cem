


cdef extern from "cem/bmi_cem.h":
    ctypedef struct BMI_Model:
        pass

    BMI_Model* register_bmi_cem(BMI_Model *model)


