#ifndef __WDONG_DIST__
#define __WDONG_DIST__

/* type = int | float */
extern int32_t chunk_cnt [];

/*
#if sizeof(chunk_t) != 1
#error If you changed chunk_t to other types, update dist_asym_* as well.
#endif
*/

static inline int32_t dist_hamming (cass_size_t n, const chunk_t *c1, const chunk_t *c2)
/* n = M / CHUNK_BIT */
{
    //printf("dist_hamming %d\n",n);
	cass_size_t dist = 0, i;
	for (i = 0; i < n; i++)
	{
		dist += chunk_cnt[c1[i] ^ c2[i]];
	}
	return dist;
}

/* Generate distance functions with/without weight/threshold */

static const float LVA_wrapper_float_star(const float* loc)
{
    return *loc;
}

static const int LVA_wrapper_int_star(const int* loc)
{
    return *loc;
}


static float dist_L2_float_LVA (cass_size_t D, const float *P1, const float *P2)
{
    //printf("here\n");
    float result;
    float tmp;
    cass_size_t i;
    result = 0;
    for (i = 0; i < D; i++)
    {
        tmp = LVA_wrapper_float_star(&(P1[i])) - LVA_wrapper_float_star(&(P2[i]));
        tmp *= tmp;
        result += tmp;
    }
    return sqrt(result);
}

static  int dist_L2_int_LVA (cass_size_t D, const int *P1, const int *P2)
{
    //printf("here\n");
    int result;
    int tmp;
    cass_size_t i;
    result = 0;
    for (i = 0; i < D; i++)
    {
        tmp = LVA_wrapper_int_star(&(P1[i])) - LVA_wrapper_int_star(&(P2[i]));
        tmp *= tmp;
        result += tmp;
    }
    return sqrt(result);
}



#define GEN_DIST(type)\
\
static inline type dist_L2_##type (cass_size_t D, const type *P1, const type *P2)\
{\
	type result;\
	type tmp;\
	cass_size_t i;\
	result = 0;\
	for (i = 0; i < D; i++)\
	{\
		tmp = P1[i] - P2[i];\
		tmp *= tmp;\
		result += tmp;\
	}\
	return sqrt(result);\
}\
\
static inline type dist_L2_##type##_W (cass_size_t D, const type *P1, const type *P2, const type *weight)\
{\
	type result;\
	type tmp;\
	cass_size_t i;\
	result = 0;\
	for (i = 0; i < D; i++)\
	{\
		tmp = P1[i] - P2[i];\
		tmp *= tmp;\
		tmp *= weight[i];\
		result += tmp;\
	}\
	return sqrt(result);\
}\
\
static inline type dist_L2_##type##_T (cass_size_t D, const type *P1, const type *P2, type T)\
{\
	type result;\
	type tmp;\
	cass_size_t i;\
	result = 0;\
	for (i = 0; i < D; i++)\
	{\
		tmp = P1[i] - P2[i];\
		tmp *= tmp;\
		result += tmp;\
		if (result > T * T) break;\
	}\
	return sqrt(result);\
}\
\
static inline type dist_L1_##type (cass_size_t D, const type *P1, const type *P2)\
{\
	type result;\
	type tmp;\
	cass_size_t i;\
	result = 0;\
	for (i = 0; i < D; i++)\
	{\
		tmp = P1[i] - P2[i];\
		result += tmp >= 0 ? tmp : -tmp;\
	}\
	return result;\
}\
\
static inline type dist_L1_##type##_W (cass_size_t D, const type *P1, const type *P2, const type *weight)\
{\
	type result;\
	type tmp;\
	cass_size_t i;\
	result = 0;\
	for (i = 0; i < D; i++)\
	{\
		tmp = P1[i] - P2[i];\
		result += weight[i] * (tmp >= 0 ? tmp : -tmp);\
	}\
	return result;\
}\
static inline type dist_cos_##type (cass_size_t D, const type *P1, const type *P2)\
{\
	type result;\
	cass_size_t i;\
	result = 0;\
	for (i = 0; i < D; i++)\
	{\
		result += P1[i]*P2[i];\
	}\
	return result;\
}\


GEN_DIST(int32_t);
GEN_DIST(float);

#endif

