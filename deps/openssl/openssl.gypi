{
  'variables': {
    'openssl_sources': [
      'openssl/ssl/bio_ssl.c',
      'openssl/ssl/d1_both.c',
      'openssl/ssl/d1_clnt.c',
      'openssl/ssl/d1_enc.c',
      'openssl/ssl/d1_lib.c',
      'openssl/ssl/d1_meth.c',
      'openssl/ssl/d1_pkt.c',
      'openssl/ssl/d1_srtp.c',
      'openssl/ssl/d1_srvr.c',
      'openssl/ssl/kssl.c',
      'openssl/ssl/s23_clnt.c',
      'openssl/ssl/s23_lib.c',
      'openssl/ssl/s23_meth.c',
      'openssl/ssl/s23_pkt.c',
      'openssl/ssl/s23_srvr.c',
      'openssl/ssl/s2_clnt.c',
      'openssl/ssl/s2_enc.c',
      'openssl/ssl/s2_lib.c',
      'openssl/ssl/s2_meth.c',
      'openssl/ssl/s2_pkt.c',
      'openssl/ssl/s2_srvr.c',
      'openssl/ssl/s3_both.c',
      'openssl/ssl/s3_clnt.c',
      'openssl/ssl/s3_enc.c',
      'openssl/ssl/s3_lib.c',
      'openssl/ssl/s3_meth.c',
      'openssl/ssl/s3_pkt.c',
      'openssl/ssl/s3_srvr.c',
      'openssl/ssl/s3_cbc.c',
      'openssl/ssl/ssl_algs.c',
      'openssl/ssl/ssl_asn1.c',
      'openssl/ssl/ssl_cert.c',
      'openssl/ssl/ssl_ciph.c',
      'openssl/ssl/ssl_err.c',
      'openssl/ssl/ssl_err2.c',
      'openssl/ssl/ssl_lib.c',
      'openssl/ssl/ssl_rsa.c',
      'openssl/ssl/ssl_sess.c',
      'openssl/ssl/ssl_stat.c',
      'openssl/ssl/ssl_txt.c',
      'openssl/ssl/t1_clnt.c',
      'openssl/ssl/t1_enc.c',
      'openssl/ssl/t1_lib.c',
      'openssl/ssl/t1_meth.c',
      'openssl/ssl/t1_reneg.c',
      'openssl/ssl/t1_srvr.c',
      'openssl/ssl/tls_srp.c',
      'openssl/crypto/aes/aes_cfb.c',
      'openssl/crypto/aes/aes_ctr.c',
      'openssl/crypto/aes/aes_ecb.c',
      'openssl/crypto/aes/aes_ige.c',
      'openssl/crypto/aes/aes_misc.c',
      'openssl/crypto/aes/aes_ofb.c',
      'openssl/crypto/aes/aes_wrap.c',
      'openssl/crypto/asn1/a_bitstr.c',
      'openssl/crypto/asn1/a_bool.c',
      'openssl/crypto/asn1/a_bytes.c',
      'openssl/crypto/asn1/a_d2i_fp.c',
      'openssl/crypto/asn1/a_digest.c',
      'openssl/crypto/asn1/a_dup.c',
      'openssl/crypto/asn1/a_enum.c',
      'openssl/crypto/asn1/a_gentm.c',
      'openssl/crypto/asn1/a_i2d_fp.c',
      'openssl/crypto/asn1/a_int.c',
      'openssl/crypto/asn1/a_mbstr.c',
      'openssl/crypto/asn1/a_object.c',
      'openssl/crypto/asn1/a_octet.c',
      'openssl/crypto/asn1/a_print.c',
      'openssl/crypto/asn1/a_set.c',
      'openssl/crypto/asn1/a_sign.c',
      'openssl/crypto/asn1/a_strex.c',
      'openssl/crypto/asn1/a_strnid.c',
      'openssl/crypto/asn1/a_time.c',
      'openssl/crypto/asn1/a_type.c',
      'openssl/crypto/asn1/a_utctm.c',
      'openssl/crypto/asn1/a_utf8.c',
      'openssl/crypto/asn1/a_verify.c',
      'openssl/crypto/asn1/ameth_lib.c',
      'openssl/crypto/asn1/asn1_err.c',
      'openssl/crypto/asn1/asn1_gen.c',
      'openssl/crypto/asn1/asn1_lib.c',
      'openssl/crypto/asn1/asn1_par.c',
      'openssl/crypto/asn1/asn_mime.c',
      'openssl/crypto/asn1/asn_moid.c',
      'openssl/crypto/asn1/asn_pack.c',
      'openssl/crypto/asn1/bio_asn1.c',
      'openssl/crypto/asn1/bio_ndef.c',
      'openssl/crypto/asn1/d2i_pr.c',
      'openssl/crypto/asn1/d2i_pu.c',
      'openssl/crypto/asn1/evp_asn1.c',
      'openssl/crypto/asn1/f_enum.c',
      'openssl/crypto/asn1/f_int.c',
      'openssl/crypto/asn1/f_string.c',
      'openssl/crypto/asn1/i2d_pr.c',
      'openssl/crypto/asn1/i2d_pu.c',
      'openssl/crypto/asn1/n_pkey.c',
      'openssl/crypto/asn1/nsseq.c',
      'openssl/crypto/asn1/p5_pbe.c',
      'openssl/crypto/asn1/p5_pbev2.c',
      'openssl/crypto/asn1/p8_pkey.c',
      'openssl/crypto/asn1/t_bitst.c',
      'openssl/crypto/asn1/t_crl.c',
      'openssl/crypto/asn1/t_pkey.c',
      'openssl/crypto/asn1/t_req.c',
      'openssl/crypto/asn1/t_spki.c',
      'openssl/crypto/asn1/t_x509.c',
      'openssl/crypto/asn1/t_x509a.c',
      'openssl/crypto/asn1/tasn_dec.c',
      'openssl/crypto/asn1/tasn_enc.c',
      'openssl/crypto/asn1/tasn_fre.c',
      'openssl/crypto/asn1/tasn_new.c',
      'openssl/crypto/asn1/tasn_prn.c',
      'openssl/crypto/asn1/tasn_typ.c',
      'openssl/crypto/asn1/tasn_utl.c',
      'openssl/crypto/asn1/x_algor.c',
      'openssl/crypto/asn1/x_attrib.c',
      'openssl/crypto/asn1/x_bignum.c',
      'openssl/crypto/asn1/x_crl.c',
      'openssl/crypto/asn1/x_exten.c',
      'openssl/crypto/asn1/x_info.c',
      'openssl/crypto/asn1/x_long.c',
      'openssl/crypto/asn1/x_name.c',
      'openssl/crypto/asn1/x_nx509.c',
      'openssl/crypto/asn1/x_pkey.c',
      'openssl/crypto/asn1/x_pubkey.c',
      'openssl/crypto/asn1/x_req.c',
      'openssl/crypto/asn1/x_sig.c',
      'openssl/crypto/asn1/x_spki.c',
      'openssl/crypto/asn1/x_val.c',
      'openssl/crypto/asn1/x_x509.c',
      'openssl/crypto/asn1/x_x509a.c',
      'openssl/crypto/bf/bf_cfb64.c',
      'openssl/crypto/bf/bf_ecb.c',
      'openssl/crypto/bf/bf_ofb64.c',
      'openssl/crypto/bf/bf_skey.c',
      'openssl/crypto/bio/b_dump.c',
      'openssl/crypto/bio/b_print.c',
      'openssl/crypto/bio/b_sock.c',
      'openssl/crypto/bio/bf_buff.c',
      'openssl/crypto/bio/bf_nbio.c',
      'openssl/crypto/bio/bf_null.c',
      'openssl/crypto/bio/bio_cb.c',
      'openssl/crypto/bio/bio_err.c',
      'openssl/crypto/bio/bio_lib.c',
      'openssl/crypto/bio/bss_acpt.c',
      'openssl/crypto/bio/bss_bio.c',
      'openssl/crypto/bio/bss_conn.c',
      'openssl/crypto/bio/bss_dgram.c',
      'openssl/crypto/bio/bss_fd.c',
      'openssl/crypto/bio/bss_file.c',
      'openssl/crypto/bio/bss_log.c',
      'openssl/crypto/bio/bss_mem.c',
      'openssl/crypto/bio/bss_null.c',
      'openssl/crypto/bio/bss_sock.c',
      'openssl/crypto/bn/bn_add.c',
      'openssl/crypto/bn/bn_blind.c',
      'openssl/crypto/bn/bn_const.c',
      'openssl/crypto/bn/bn_ctx.c',
      'openssl/crypto/bn/bn_depr.c',
      'openssl/crypto/bn/bn_div.c',
      'openssl/crypto/bn/bn_err.c',
      'openssl/crypto/bn/bn_exp.c',
      'openssl/crypto/bn/bn_exp2.c',
      'openssl/crypto/bn/bn_gcd.c',
      'openssl/crypto/bn/bn_gf2m.c',
      'openssl/crypto/bn/bn_kron.c',
      'openssl/crypto/bn/bn_lib.c',
      'openssl/crypto/bn/bn_mod.c',
      'openssl/crypto/bn/bn_mont.c',
      'openssl/crypto/bn/bn_mpi.c',
      'openssl/crypto/bn/bn_mul.c',
      'openssl/crypto/bn/bn_nist.c',
      'openssl/crypto/bn/bn_prime.c',
      'openssl/crypto/bn/bn_print.c',
      'openssl/crypto/bn/bn_rand.c',
      'openssl/crypto/bn/bn_recp.c',
      'openssl/crypto/bn/bn_shift.c',
      'openssl/crypto/bn/bn_sqr.c',
      'openssl/crypto/bn/bn_sqrt.c',
      'openssl/crypto/bn/bn_word.c',
      'openssl/crypto/bn/bn_x931p.c',
      'openssl/crypto/buffer/buf_err.c',
      'openssl/crypto/buffer/buf_str.c',
      'openssl/crypto/buffer/buffer.c',
      'openssl/crypto/camellia/cmll_cfb.c',
      'openssl/crypto/camellia/cmll_ctr.c',
      'openssl/crypto/camellia/cmll_ecb.c',
      'openssl/crypto/camellia/cmll_ofb.c',
      'openssl/crypto/camellia/cmll_utl.c',
      'openssl/crypto/cast/c_cfb64.c',
      'openssl/crypto/cast/c_ecb.c',
      'openssl/crypto/cast/c_ofb64.c',
      'openssl/crypto/cast/c_skey.c',
      'openssl/crypto/cmac/cm_ameth.c',
      'openssl/crypto/cmac/cm_pmeth.c',
      'openssl/crypto/cmac/cmac.c',
      'openssl/crypto/cms/cms_asn1.c',
      'openssl/crypto/cms/cms_att.c',
      'openssl/crypto/cms/cms_cd.c',
      'openssl/crypto/cms/cms_dd.c',
      'openssl/crypto/cms/cms_enc.c',
      'openssl/crypto/cms/cms_env.c',
      'openssl/crypto/cms/cms_err.c',
      'openssl/crypto/cms/cms_ess.c',
      'openssl/crypto/cms/cms_io.c',
      'openssl/crypto/cms/cms_lib.c',
      'openssl/crypto/cms/cms_pwri.c',
      'openssl/crypto/cms/cms_sd.c',
      'openssl/crypto/cms/cms_smime.c',
      'openssl/crypto/comp/c_rle.c',
      'openssl/crypto/comp/c_zlib.c',
      'openssl/crypto/comp/comp_err.c',
      'openssl/crypto/comp/comp_lib.c',
      'openssl/crypto/conf/conf_api.c',
      'openssl/crypto/conf/conf_def.c',
      'openssl/crypto/conf/conf_err.c',
      'openssl/crypto/conf/conf_lib.c',
      'openssl/crypto/conf/conf_mall.c',
      'openssl/crypto/conf/conf_mod.c',
      'openssl/crypto/conf/conf_sap.c',
      'openssl/crypto/cpt_err.c',
      'openssl/crypto/cryptlib.c',
      'openssl/crypto/cversion.c',
      'openssl/crypto/des/cbc_cksm.c',
      'openssl/crypto/des/cbc_enc.c',
      'openssl/crypto/des/cfb64ede.c',
      'openssl/crypto/des/cfb64enc.c',
      'openssl/crypto/des/cfb_enc.c',
      'openssl/crypto/des/des_old.c',
      'openssl/crypto/des/des_old2.c',
      'openssl/crypto/des/ecb3_enc.c',
      'openssl/crypto/des/ecb_enc.c',
      'openssl/crypto/des/ede_cbcm_enc.c',
      'openssl/crypto/des/enc_read.c',
      'openssl/crypto/des/enc_writ.c',
      'openssl/crypto/des/fcrypt.c',
      'openssl/crypto/des/ofb64ede.c',
      'openssl/crypto/des/ofb64enc.c',
      'openssl/crypto/des/ofb_enc.c',
      'openssl/crypto/des/pcbc_enc.c',
      'openssl/crypto/des/qud_cksm.c',
      'openssl/crypto/des/rand_key.c',
      'openssl/crypto/des/read2pwd.c',
      'openssl/crypto/des/rpc_enc.c',
      'openssl/crypto/des/set_key.c',
      'openssl/crypto/des/str2key.c',
      'openssl/crypto/des/xcbc_enc.c',
      'openssl/crypto/dh/dh_ameth.c',
      'openssl/crypto/dh/dh_asn1.c',
      'openssl/crypto/dh/dh_check.c',
      'openssl/crypto/dh/dh_depr.c',
      'openssl/crypto/dh/dh_err.c',
      'openssl/crypto/dh/dh_gen.c',
      'openssl/crypto/dh/dh_key.c',
      'openssl/crypto/dh/dh_lib.c',
      'openssl/crypto/dh/dh_pmeth.c',
      'openssl/crypto/dh/dh_prn.c',
      'openssl/crypto/dsa/dsa_ameth.c',
      'openssl/crypto/dsa/dsa_asn1.c',
      'openssl/crypto/dsa/dsa_depr.c',
      'openssl/crypto/dsa/dsa_err.c',
      'openssl/crypto/dsa/dsa_gen.c',
      'openssl/crypto/dsa/dsa_key.c',
      'openssl/crypto/dsa/dsa_lib.c',
      'openssl/crypto/dsa/dsa_ossl.c',
      'openssl/crypto/dsa/dsa_pmeth.c',
      'openssl/crypto/dsa/dsa_prn.c',
      'openssl/crypto/dsa/dsa_sign.c',
      'openssl/crypto/dsa/dsa_vrf.c',
      'openssl/crypto/dso/dso_beos.c',
      'openssl/crypto/dso/dso_dl.c',
      'openssl/crypto/dso/dso_dlfcn.c',
      'openssl/crypto/dso/dso_err.c',
      'openssl/crypto/dso/dso_lib.c',
      'openssl/crypto/dso/dso_null.c',
      'openssl/crypto/dso/dso_openssl.c',
      'openssl/crypto/dso/dso_vms.c',
      'openssl/crypto/dso/dso_win32.c',
      'openssl/crypto/ebcdic.c',
      'openssl/crypto/ec/ec2_mult.c',
      'openssl/crypto/ec/ec2_oct.c',
      'openssl/crypto/ec/ec2_smpl.c',
      'openssl/crypto/ec/ec_ameth.c',
      'openssl/crypto/ec/ec_asn1.c',
      'openssl/crypto/ec/ec_check.c',
      'openssl/crypto/ec/ec_curve.c',
      'openssl/crypto/ec/ec_cvt.c',
      'openssl/crypto/ec/ec_err.c',
      'openssl/crypto/ec/ec_key.c',
      'openssl/crypto/ec/ec_lib.c',
      'openssl/crypto/ec/ec_mult.c',
      'openssl/crypto/ec/ec_oct.c',
      'openssl/crypto/ec/ec_pmeth.c',
      'openssl/crypto/ec/ec_print.c',
      'openssl/crypto/ec/eck_prn.c',
      'openssl/crypto/ec/ecp_mont.c',
      'openssl/crypto/ec/ecp_nist.c',
      'openssl/crypto/ec/ecp_nistp224.c',
      'openssl/crypto/ec/ecp_nistp256.c',
      'openssl/crypto/ec/ecp_nistp521.c',
      'openssl/crypto/ec/ecp_nistputil.c',
      'openssl/crypto/ec/ecp_oct.c',
      'openssl/crypto/ec/ecp_smpl.c',
      'openssl/crypto/ecdh/ech_err.c',
      'openssl/crypto/ecdh/ech_key.c',
      'openssl/crypto/ecdh/ech_lib.c',
      'openssl/crypto/ecdh/ech_ossl.c',
      'openssl/crypto/ecdsa/ecs_asn1.c',
      'openssl/crypto/ecdsa/ecs_err.c',
      'openssl/crypto/ecdsa/ecs_lib.c',
      'openssl/crypto/ecdsa/ecs_ossl.c',
      'openssl/crypto/ecdsa/ecs_sign.c',
      'openssl/crypto/ecdsa/ecs_vrf.c',
      'openssl/crypto/engine/eng_all.c',
      'openssl/crypto/engine/eng_cnf.c',
      'openssl/crypto/engine/eng_cryptodev.c',
      'openssl/crypto/engine/eng_ctrl.c',
      'openssl/crypto/engine/eng_dyn.c',
      'openssl/crypto/engine/eng_err.c',
      'openssl/crypto/engine/eng_fat.c',
      'openssl/crypto/engine/eng_init.c',
      'openssl/crypto/engine/eng_lib.c',
      'openssl/crypto/engine/eng_list.c',
      'openssl/crypto/engine/eng_openssl.c',
      'openssl/crypto/engine/eng_pkey.c',
      'openssl/crypto/engine/eng_rdrand.c',
      'openssl/crypto/engine/eng_rsax.c',
      'openssl/crypto/engine/eng_table.c',
      'openssl/crypto/engine/tb_asnmth.c',
      'openssl/crypto/engine/tb_cipher.c',
      'openssl/crypto/engine/tb_dh.c',
      'openssl/crypto/engine/tb_digest.c',
      'openssl/crypto/engine/tb_dsa.c',
      'openssl/crypto/engine/tb_ecdh.c',
      'openssl/crypto/engine/tb_ecdsa.c',
      'openssl/crypto/engine/tb_pkmeth.c',
      'openssl/crypto/engine/tb_rand.c',
      'openssl/crypto/engine/tb_rsa.c',
      'openssl/crypto/engine/tb_store.c',
      'openssl/crypto/err/err.c',
      'openssl/crypto/err/err_all.c',
      'openssl/crypto/err/err_prn.c',
      'openssl/crypto/evp/bio_b64.c',
      'openssl/crypto/evp/bio_enc.c',
      'openssl/crypto/evp/bio_md.c',
      'openssl/crypto/evp/bio_ok.c',
      'openssl/crypto/evp/c_all.c',
      'openssl/crypto/evp/c_allc.c',
      'openssl/crypto/evp/c_alld.c',
      'openssl/crypto/evp/digest.c',
      'openssl/crypto/evp/e_aes.c',
      'openssl/crypto/evp/e_aes_cbc_hmac_sha1.c',
      'openssl/crypto/evp/e_bf.c',
      'openssl/crypto/evp/e_camellia.c',
      'openssl/crypto/evp/e_cast.c',
      'openssl/crypto/evp/e_des.c',
      'openssl/crypto/evp/e_des3.c',
      'openssl/crypto/evp/e_idea.c',
      'openssl/crypto/evp/e_null.c',
      'openssl/crypto/evp/e_old.c',
      'openssl/crypto/evp/e_rc2.c',
      'openssl/crypto/evp/e_rc4.c',
      'openssl/crypto/evp/e_rc4_hmac_md5.c',
      'openssl/crypto/evp/e_rc5.c',
      'openssl/crypto/evp/e_seed.c',
      'openssl/crypto/evp/e_xcbc_d.c',
      'openssl/crypto/evp/encode.c',
      'openssl/crypto/evp/evp_acnf.c',
      'openssl/crypto/evp/evp_cnf.c',
      'openssl/crypto/evp/evp_enc.c',
      'openssl/crypto/evp/evp_err.c',
      'openssl/crypto/evp/evp_fips.c',
      'openssl/crypto/evp/evp_key.c',
      'openssl/crypto/evp/evp_lib.c',
      'openssl/crypto/evp/evp_pbe.c',
      'openssl/crypto/evp/evp_pkey.c',
      'openssl/crypto/evp/m_dss.c',
      'openssl/crypto/evp/m_dss1.c',
      'openssl/crypto/evp/m_ecdsa.c',
      'openssl/crypto/evp/m_md2.c',
      'openssl/crypto/evp/m_md4.c',
      'openssl/crypto/evp/m_md5.c',
      'openssl/crypto/evp/m_mdc2.c',
      'openssl/crypto/evp/m_null.c',
      'openssl/crypto/evp/m_ripemd.c',
      'openssl/crypto/evp/m_sha.c',
      'openssl/crypto/evp/m_sha1.c',
      'openssl/crypto/evp/m_sigver.c',
      'openssl/crypto/evp/m_wp.c',
      'openssl/crypto/evp/names.c',
      'openssl/crypto/evp/p5_crpt.c',
      'openssl/crypto/evp/p5_crpt2.c',
      'openssl/crypto/evp/p_dec.c',
      'openssl/crypto/evp/p_enc.c',
      'openssl/crypto/evp/p_lib.c',
      'openssl/crypto/evp/p_open.c',
      'openssl/crypto/evp/p_seal.c',
      'openssl/crypto/evp/p_sign.c',
      'openssl/crypto/evp/p_verify.c',
      'openssl/crypto/evp/pmeth_fn.c',
      'openssl/crypto/evp/pmeth_gn.c',
      'openssl/crypto/evp/pmeth_lib.c',
      'openssl/crypto/ex_data.c',
      'openssl/crypto/fips_ers.c',
      'openssl/crypto/hmac/hm_ameth.c',
      'openssl/crypto/hmac/hm_pmeth.c',
      'openssl/crypto/hmac/hmac.c',
      'openssl/crypto/idea/i_cbc.c',
      'openssl/crypto/idea/i_cfb64.c',
      'openssl/crypto/idea/i_ecb.c',
      'openssl/crypto/idea/i_ofb64.c',
      'openssl/crypto/idea/i_skey.c',
      'openssl/crypto/krb5/krb5_asn.c',
      'openssl/crypto/lhash/lh_stats.c',
      'openssl/crypto/lhash/lhash.c',
      'openssl/crypto/md2/md2_dgst.c',
      'openssl/crypto/md2/md2_one.c',
      'openssl/crypto/md4/md4_dgst.c',
      'openssl/crypto/md4/md4_one.c',
      'openssl/crypto/md5/md5_dgst.c',
      'openssl/crypto/md5/md5_one.c',
      'openssl/crypto/mdc2/mdc2_one.c',
      'openssl/crypto/mdc2/mdc2dgst.c',
      'openssl/crypto/mem.c',
      'openssl/crypto/mem_dbg.c',
      'openssl/crypto/modes/cbc128.c',
      'openssl/crypto/modes/ccm128.c',
      'openssl/crypto/modes/cfb128.c',
      'openssl/crypto/modes/ctr128.c',
      'openssl/crypto/modes/cts128.c',
      'openssl/crypto/modes/gcm128.c',
      'openssl/crypto/modes/ofb128.c',
      'openssl/crypto/modes/xts128.c',
      'openssl/crypto/o_dir.c',
      'openssl/crypto/o_fips.c',
      'openssl/crypto/o_init.c',
      'openssl/crypto/o_str.c',
      'openssl/crypto/o_time.c',
      'openssl/crypto/objects/o_names.c',
      'openssl/crypto/objects/obj_dat.c',
      'openssl/crypto/objects/obj_err.c',
      'openssl/crypto/objects/obj_lib.c',
      'openssl/crypto/objects/obj_xref.c',
      'openssl/crypto/ocsp/ocsp_asn.c',
      'openssl/crypto/ocsp/ocsp_cl.c',
      'openssl/crypto/ocsp/ocsp_err.c',
      'openssl/crypto/ocsp/ocsp_ext.c',
      'openssl/crypto/ocsp/ocsp_ht.c',
      'openssl/crypto/ocsp/ocsp_lib.c',
      'openssl/crypto/ocsp/ocsp_prn.c',
      'openssl/crypto/ocsp/ocsp_srv.c',
      'openssl/crypto/ocsp/ocsp_vfy.c',
      'openssl/crypto/pem/pem_all.c',
      'openssl/crypto/pem/pem_err.c',
      'openssl/crypto/pem/pem_info.c',
      'openssl/crypto/pem/pem_lib.c',
      'openssl/crypto/pem/pem_oth.c',
      'openssl/crypto/pem/pem_pk8.c',
      'openssl/crypto/pem/pem_pkey.c',
      'openssl/crypto/pem/pem_seal.c',
      'openssl/crypto/pem/pem_sign.c',
      'openssl/crypto/pem/pem_x509.c',
      'openssl/crypto/pem/pem_xaux.c',
      'openssl/crypto/pem/pvkfmt.c',
      'openssl/crypto/pkcs12/p12_add.c',
      'openssl/crypto/pkcs12/p12_asn.c',
      'openssl/crypto/pkcs12/p12_attr.c',
      'openssl/crypto/pkcs12/p12_crpt.c',
      'openssl/crypto/pkcs12/p12_crt.c',
      'openssl/crypto/pkcs12/p12_decr.c',
      'openssl/crypto/pkcs12/p12_init.c',
      'openssl/crypto/pkcs12/p12_key.c',
      'openssl/crypto/pkcs12/p12_kiss.c',
      'openssl/crypto/pkcs12/p12_mutl.c',
      'openssl/crypto/pkcs12/p12_npas.c',
      'openssl/crypto/pkcs12/p12_p8d.c',
      'openssl/crypto/pkcs12/p12_p8e.c',
      'openssl/crypto/pkcs12/p12_utl.c',
      'openssl/crypto/pkcs12/pk12err.c',
      'openssl/crypto/pkcs7/bio_pk7.c',
      'openssl/crypto/pkcs7/pk7_asn1.c',
      'openssl/crypto/pkcs7/pk7_attr.c',
      'openssl/crypto/pkcs7/pk7_doit.c',
      'openssl/crypto/pkcs7/pk7_lib.c',
      'openssl/crypto/pkcs7/pk7_mime.c',
      'openssl/crypto/pkcs7/pk7_smime.c',
      'openssl/crypto/pkcs7/pkcs7err.c',
      'openssl/crypto/pqueue/pqueue.c',
      'openssl/crypto/rand/md_rand.c',
      'openssl/crypto/rand/rand_egd.c',
      'openssl/crypto/rand/rand_err.c',
      'openssl/crypto/rand/rand_lib.c',
      'openssl/crypto/rand/rand_nw.c',
      'openssl/crypto/rand/rand_os2.c',
      'openssl/crypto/rand/rand_unix.c',
      'openssl/crypto/rand/rand_win.c',
      'openssl/crypto/rand/randfile.c',
      'openssl/crypto/rc2/rc2_cbc.c',
      'openssl/crypto/rc2/rc2_ecb.c',
      'openssl/crypto/rc2/rc2_skey.c',
      'openssl/crypto/rc2/rc2cfb64.c',
      'openssl/crypto/rc2/rc2ofb64.c',
      'openssl/crypto/rc4/rc4_utl.c',
      'openssl/crypto/ripemd/rmd_dgst.c',
      'openssl/crypto/ripemd/rmd_one.c',
      'openssl/crypto/rsa/rsa_ameth.c',
      'openssl/crypto/rsa/rsa_asn1.c',
      'openssl/crypto/rsa/rsa_chk.c',
      'openssl/crypto/rsa/rsa_crpt.c',
      'openssl/crypto/rsa/rsa_depr.c',
      'openssl/crypto/rsa/rsa_eay.c',
      'openssl/crypto/rsa/rsa_err.c',
      'openssl/crypto/rsa/rsa_gen.c',
      'openssl/crypto/rsa/rsa_lib.c',
      'openssl/crypto/rsa/rsa_none.c',
      'openssl/crypto/rsa/rsa_null.c',
      'openssl/crypto/rsa/rsa_oaep.c',
      'openssl/crypto/rsa/rsa_pk1.c',
      'openssl/crypto/rsa/rsa_pmeth.c',
      'openssl/crypto/rsa/rsa_prn.c',
      'openssl/crypto/rsa/rsa_pss.c',
      'openssl/crypto/rsa/rsa_saos.c',
      'openssl/crypto/rsa/rsa_sign.c',
      'openssl/crypto/rsa/rsa_ssl.c',
      'openssl/crypto/rsa/rsa_x931.c',
      'openssl/crypto/seed/seed.c',
      'openssl/crypto/seed/seed_cbc.c',
      'openssl/crypto/seed/seed_cfb.c',
      'openssl/crypto/seed/seed_ecb.c',
      'openssl/crypto/seed/seed_ofb.c',
      'openssl/crypto/sha/sha1_one.c',
      'openssl/crypto/sha/sha1dgst.c',
      'openssl/crypto/sha/sha256.c',
      'openssl/crypto/sha/sha512.c',
      'openssl/crypto/sha/sha_dgst.c',
      'openssl/crypto/sha/sha_one.c',
      'openssl/crypto/srp/srp_lib.c',
      'openssl/crypto/srp/srp_vfy.c',
      'openssl/crypto/stack/stack.c',
      'openssl/crypto/store/str_err.c',
      'openssl/crypto/store/str_lib.c',
      'openssl/crypto/store/str_mem.c',
      'openssl/crypto/store/str_meth.c',
      'openssl/crypto/ts/ts_asn1.c',
      'openssl/crypto/ts/ts_conf.c',
      'openssl/crypto/ts/ts_err.c',
      'openssl/crypto/ts/ts_lib.c',
      'openssl/crypto/ts/ts_req_print.c',
      'openssl/crypto/ts/ts_req_utils.c',
      'openssl/crypto/ts/ts_rsp_print.c',
      'openssl/crypto/ts/ts_rsp_sign.c',
      'openssl/crypto/ts/ts_rsp_utils.c',
      'openssl/crypto/ts/ts_rsp_verify.c',
      'openssl/crypto/ts/ts_verify_ctx.c',
      'openssl/crypto/txt_db/txt_db.c',
      'openssl/crypto/ui/ui_compat.c',
      'openssl/crypto/ui/ui_err.c',
      'openssl/crypto/ui/ui_lib.c',
      'openssl/crypto/ui/ui_openssl.c',
      'openssl/crypto/ui/ui_util.c',
      'openssl/crypto/uid.c',
      'openssl/crypto/whrlpool/wp_dgst.c',
      'openssl/crypto/x509/by_dir.c',
      'openssl/crypto/x509/by_file.c',
      'openssl/crypto/x509/x509_att.c',
      'openssl/crypto/x509/x509_cmp.c',
      'openssl/crypto/x509/x509_d2.c',
      'openssl/crypto/x509/x509_def.c',
      'openssl/crypto/x509/x509_err.c',
      'openssl/crypto/x509/x509_ext.c',
      'openssl/crypto/x509/x509_lu.c',
      'openssl/crypto/x509/x509_obj.c',
      'openssl/crypto/x509/x509_r2x.c',
      'openssl/crypto/x509/x509_req.c',
      'openssl/crypto/x509/x509_set.c',
      'openssl/crypto/x509/x509_trs.c',
      'openssl/crypto/x509/x509_txt.c',
      'openssl/crypto/x509/x509_v3.c',
      'openssl/crypto/x509/x509_vfy.c',
      'openssl/crypto/x509/x509_vpm.c',
      'openssl/crypto/x509/x509cset.c',
      'openssl/crypto/x509/x509name.c',
      'openssl/crypto/x509/x509rset.c',
      'openssl/crypto/x509/x509spki.c',
      'openssl/crypto/x509/x509type.c',
      'openssl/crypto/x509/x_all.c',
      'openssl/crypto/x509v3/pcy_cache.c',
      'openssl/crypto/x509v3/pcy_data.c',
      'openssl/crypto/x509v3/pcy_lib.c',
      'openssl/crypto/x509v3/pcy_map.c',
      'openssl/crypto/x509v3/pcy_node.c',
      'openssl/crypto/x509v3/pcy_tree.c',
      'openssl/crypto/x509v3/v3_addr.c',
      'openssl/crypto/x509v3/v3_akey.c',
      'openssl/crypto/x509v3/v3_akeya.c',
      'openssl/crypto/x509v3/v3_alt.c',
      'openssl/crypto/x509v3/v3_asid.c',
      'openssl/crypto/x509v3/v3_bcons.c',
      'openssl/crypto/x509v3/v3_bitst.c',
      'openssl/crypto/x509v3/v3_conf.c',
      'openssl/crypto/x509v3/v3_cpols.c',
      'openssl/crypto/x509v3/v3_crld.c',
      'openssl/crypto/x509v3/v3_enum.c',
      'openssl/crypto/x509v3/v3_extku.c',
      'openssl/crypto/x509v3/v3_genn.c',
      'openssl/crypto/x509v3/v3_ia5.c',
      'openssl/crypto/x509v3/v3_info.c',
      'openssl/crypto/x509v3/v3_int.c',
      'openssl/crypto/x509v3/v3_lib.c',
      'openssl/crypto/x509v3/v3_ncons.c',
      'openssl/crypto/x509v3/v3_ocsp.c',
      'openssl/crypto/x509v3/v3_pci.c',
      'openssl/crypto/x509v3/v3_pcia.c',
      'openssl/crypto/x509v3/v3_pcons.c',
      'openssl/crypto/x509v3/v3_pku.c',
      'openssl/crypto/x509v3/v3_pmaps.c',
      'openssl/crypto/x509v3/v3_prn.c',
      'openssl/crypto/x509v3/v3_purp.c',
      'openssl/crypto/x509v3/v3_skey.c',
      'openssl/crypto/x509v3/v3_sxnet.c',
      'openssl/crypto/x509v3/v3_utl.c',
      'openssl/crypto/x509v3/v3err.c',
      'openssl/engines/e_4758cca.c',
      'openssl/engines/e_aep.c',
      'openssl/engines/e_atalla.c',
      'openssl/engines/e_capi.c',
      'openssl/engines/e_chil.c',
      'openssl/engines/e_cswift.c',
      'openssl/engines/e_gmp.c',
      'openssl/engines/e_nuron.c',
      'openssl/engines/e_sureware.c',
      'openssl/engines/e_ubsec.c'
    ],
    'openssl_sources_no_asm': [
      'openssl/crypto/aes/aes_cbc.c',
      'openssl/crypto/aes/aes_core.c',
      'openssl/crypto/bf/bf_enc.c',
      'openssl/crypto/bn/bn_asm.c',
      'openssl/crypto/cast/c_enc.c',
      'openssl/crypto/camellia/camellia.c',
      'openssl/crypto/camellia/cmll_cbc.c',
      'openssl/crypto/camellia/cmll_misc.c',
      'openssl/crypto/des/des_enc.c',
      'openssl/crypto/des/fcrypt_b.c',
      'openssl/crypto/mem_clr.c',
      'openssl/crypto/rc4/rc4_enc.c',
      'openssl/crypto/rc4/rc4_skey.c',
      'openssl/crypto/whrlpool/wp_block.c'
    ],
    'openssl_sources_x86_elf_gas': [
      'asm/x86-elf-gas/aes/aes-586.s',
      'asm/x86-elf-gas/aes/aesni-x86.s',
      'asm/x86-elf-gas/aes/vpaes-x86.s',
      'asm/x86-elf-gas/bf/bf-686.s',
      'asm/x86-elf-gas/bn/x86-mont.s',
      'asm/x86-elf-gas/bn/x86.s',
      'asm/x86-elf-gas/camellia/cmll-x86.s',
      'asm/x86-elf-gas/cast/cast-586.s',
      'asm/x86-elf-gas/des/crypt586.s',
      'asm/x86-elf-gas/des/des-586.s',
      'asm/x86-elf-gas/md5/md5-586.s',
      'asm/x86-elf-gas/rc4/rc4-586.s',
      'asm/x86-elf-gas/rc5/rc5-586.s',
      'asm/x86-elf-gas/ripemd/rmd-586.s',
      'asm/x86-elf-gas/sha/sha1-586.s',
      'asm/x86-elf-gas/sha/sha256-586.s',
      'asm/x86-elf-gas/sha/sha512-586.s',
      'asm/x86-elf-gas/whrlpool/wp-mmx.s',
      'asm/x86-elf-gas/modes/ghash-x86.s',
      'asm/x86-elf-gas/x86cpuid.s',
      'openssl/crypto/whrlpool/wp_block.c'
    ],
    'openssl_sources_x64_elf_gas': [
      'asm/x64-elf-gas/aes/aes-x86_64.s',
      'asm/x64-elf-gas/aes/aesni-x86_64.s',
      'asm/x64-elf-gas/aes/vpaes-x86_64.s',
      'asm/x64-elf-gas/aes/bsaes-x86_64.s',
      'asm/x64-elf-gas/aes/aesni-sha1-x86_64.s',
      'asm/x64-elf-gas/bn/modexp512-x86_64.s',
      'asm/x64-elf-gas/bn/x86_64-mont.s',
      'asm/x64-elf-gas/bn/x86_64-mont5.s',
      'asm/x64-elf-gas/bn/x86_64-gf2m.s',
      'asm/x64-elf-gas/camellia/cmll-x86_64.s',
      'asm/x64-elf-gas/md5/md5-x86_64.s',
      'asm/x64-elf-gas/rc4/rc4-x86_64.s',
      'asm/x64-elf-gas/rc4/rc4-md5-x86_64.s',
      'asm/x64-elf-gas/sha/sha1-x86_64.s',
      'asm/x64-elf-gas/sha/sha256-x86_64.s',
      'asm/x64-elf-gas/sha/sha512-x86_64.s',
      'asm/x64-elf-gas/whrlpool/wp-x86_64.s',
      'asm/x64-elf-gas/modes/ghash-x86_64.s',
      'asm/x64-elf-gas/x86_64cpuid.s',
      # Non-generated asm
      'openssl/crypto/bn/asm/x86_64-gcc.c',
      # No asm available
      'openssl/crypto/bf/bf_enc.c',
      'openssl/crypto/cast/c_enc.c',
      'openssl/crypto/camellia/cmll_misc.c',
      'openssl/crypto/des/des_enc.c',
      'openssl/crypto/des/fcrypt_b.c'
    ],
    'openssl_sources_x86_macosx_gas': [
      'asm/x86-macosx-gas/aes/aes-586.s',
      'asm/x86-macosx-gas/aes/aesni-x86.s',
      'asm/x86-macosx-gas/aes/vpaes-x86.s',
      'asm/x86-macosx-gas/bf/bf-686.s',
      'asm/x86-macosx-gas/bn/x86-mont.s',
      'asm/x86-macosx-gas/bn/x86.s',
      'asm/x86-macosx-gas/camellia/cmll-x86.s',
      'asm/x86-macosx-gas/cast/cast-586.s',
      'asm/x86-macosx-gas/des/crypt586.s',
      'asm/x86-macosx-gas/des/des-586.s',
      'asm/x86-macosx-gas/md5/md5-586.s',
      'asm/x86-macosx-gas/rc4/rc4-586.s',
      'asm/x86-macosx-gas/rc5/rc5-586.s',
      'asm/x86-macosx-gas/ripemd/rmd-586.s',
      'asm/x86-macosx-gas/sha/sha1-586.s',
      'asm/x86-macosx-gas/sha/sha256-586.s',
      'asm/x86-macosx-gas/sha/sha512-586.s',
      'asm/x86-macosx-gas/whrlpool/wp-mmx.s',
      'asm/x86-macosx-gas/modes/ghash-x86.s',
      'asm/x86-macosx-gas/x86cpuid.s',
      'openssl/crypto/whrlpool/wp_block.c'
    ],
    'openssl_sources_x64_macosx_gas': [
      'asm/x64-macosx-gas/aes/aes-x86_64.s',
      'asm/x64-macosx-gas/aes/aesni-x86_64.s',
      'asm/x64-macosx-gas/aes/vpaes-x86_64.s',
      'asm/x64-macosx-gas/aes/bsaes-x86_64.s',
      'asm/x64-macosx-gas/aes/aesni-sha1-x86_64.s',
      'asm/x64-macosx-gas/bn/modexp512-x86_64.s',
      'asm/x64-macosx-gas/bn/x86_64-mont.s',
      'asm/x64-macosx-gas/bn/x86_64-mont5.s',
      'asm/x64-macosx-gas/bn/x86_64-gf2m.s',
      'asm/x64-macosx-gas/camellia/cmll-x86_64.s',
      'asm/x64-macosx-gas/md5/md5-x86_64.s',
      'asm/x64-macosx-gas/rc4/rc4-x86_64.s',
      'asm/x64-macosx-gas/rc4/rc4-md5-x86_64.s',
      'asm/x64-macosx-gas/sha/sha1-x86_64.s',
      'asm/x64-macosx-gas/sha/sha256-x86_64.s',
      'asm/x64-macosx-gas/sha/sha512-x86_64.s',
      'asm/x64-macosx-gas/whrlpool/wp-x86_64.s',
      'asm/x64-macosx-gas/modes/ghash-x86_64.s',
      'asm/x64-macosx-gas/x86_64cpuid.s',
      # Non-generated asm
      'openssl/crypto/bn/asm/x86_64-gcc.c',
      # No asm available
      'openssl/crypto/bf/bf_enc.c',
      'openssl/crypto/cast/c_enc.c',
      'openssl/crypto/camellia/cmll_misc.c',
      'openssl/crypto/des/des_enc.c',
      'openssl/crypto/des/fcrypt_b.c'
    ],
    'openssl_sources_arm_elf_gas': [
      'asm/arm-elf-gas/aes/aes-armv4.s',
      'asm/arm-elf-gas/bn/armv4-mont.s',
      'asm/arm-elf-gas/bn/armv4-gf2m.s',
      'asm/arm-elf-gas/sha/sha1-armv4-large.s',
      'asm/arm-elf-gas/sha/sha512-armv4.s',
      'asm/arm-elf-gas/sha/sha256-armv4.s',
      'asm/arm-elf-gas/modes/ghash-armv4.s',
      # No asm available
      'openssl/crypto/aes/aes_cbc.c',
      'openssl/crypto/bf/bf_enc.c',
      'openssl/crypto/bn/bn_asm.c',
      'openssl/crypto/cast/c_enc.c',
      'openssl/crypto/camellia/camellia.c',
      'openssl/crypto/camellia/cmll_cbc.c',
      'openssl/crypto/camellia/cmll_misc.c',
      'openssl/crypto/des/des_enc.c',
      'openssl/crypto/des/fcrypt_b.c',
      'openssl/crypto/rc4/rc4_enc.c',
      'openssl/crypto/rc4/rc4_skey.c',
      'openssl/crypto/whrlpool/wp_block.c',
      # PCAP stuff
      'openssl/crypto/armcap.c',
      'openssl/crypto/armv4cpuid.S',
    ],
    'openssl_sources_x86_win32_masm': [
      'asm/x86-win32-masm/aes/aes-586.asm',
      'asm/x86-win32-masm/aes/aesni-x86.asm',
      'asm/x86-win32-masm/aes/vpaes-x86.asm',
      'asm/x86-win32-masm/bf/bf-686.asm',
      'asm/x86-win32-masm/bn/x86-mont.asm',
      'asm/x86-win32-masm/bn/x86.asm',
      'asm/x86-win32-masm/camellia/cmll-x86.asm',
      'asm/x86-win32-masm/cast/cast-586.asm',
      'asm/x86-win32-masm/des/crypt586.asm',
      'asm/x86-win32-masm/des/des-586.asm',
      'asm/x86-win32-masm/md5/md5-586.asm',
      'asm/x86-win32-masm/rc4/rc4-586.asm',
      'asm/x86-win32-masm/rc5/rc5-586.asm',
      'asm/x86-win32-masm/ripemd/rmd-586.asm',
      'asm/x86-win32-masm/sha/sha1-586.asm',
      'asm/x86-win32-masm/sha/sha256-586.asm',
      'asm/x86-win32-masm/sha/sha512-586.asm',
      'asm/x86-win32-masm/whrlpool/wp-mmx.asm',
      'asm/x86-win32-masm/modes/ghash-x86.asm',
      'asm/x86-win32-masm/x86cpuid.asm',
      'openssl/crypto/whrlpool/wp_block.c'
    ],
    'openssl_sources_x64_win32_masm': [
      'asm/x64-win32-masm/aes/aes-x86_64.asm',
      'asm/x64-win32-masm/aes/aesni-x86_64.asm',
      'asm/x64-win32-masm/aes/vpaes-x86_64.asm',
      'asm/x64-win32-masm/aes/bsaes-x86_64.asm',
      'asm/x64-win32-masm/aes/aesni-sha1-x86_64.asm',
      'asm/x64-win32-masm/bn/modexp512-x86_64.asm',
      'asm/x64-win32-masm/bn/x86_64-mont.asm',
      'asm/x64-win32-masm/bn/x86_64-mont5.asm',
      'asm/x64-win32-masm/bn/x86_64-gf2m.asm',
      'asm/x64-win32-masm/camellia/cmll-x86_64.asm',
      'asm/x64-win32-masm/md5/md5-x86_64.asm',
      'asm/x64-win32-masm/rc4/rc4-x86_64.asm',
      'asm/x64-win32-masm/rc4/rc4-md5-x86_64.asm',
      'asm/x64-win32-masm/sha/sha1-x86_64.asm',
      'asm/x64-win32-masm/sha/sha256-x86_64.asm',
      'asm/x64-win32-masm/sha/sha512-x86_64.asm',
      'asm/x64-win32-masm/whrlpool/wp-x86_64.asm',
      'asm/x64-win32-masm/modes/ghash-x86_64.asm',
      'asm/x64-win32-masm/x86_64cpuid.asm',
      # No asm available
      'openssl/crypto/bn/bn_asm.c',
      'openssl/crypto/bf/bf_enc.c',
      'openssl/crypto/cast/c_enc.c',
      'openssl/crypto/camellia/cmll_misc.c',
      'openssl/crypto/des/des_enc.c',
      'openssl/crypto/des/fcrypt_b.c'
    ],
    'openssl_cli_sources': [
      'openssl/apps/app_rand.c',
      'openssl/apps/apps.c',
      'openssl/apps/asn1pars.c',
      'openssl/apps/ca.c',
      'openssl/apps/ciphers.c',
      'openssl/apps/cms.c',
      'openssl/apps/crl.c',
      'openssl/apps/crl2p7.c',
      'openssl/apps/dgst.c',
      'openssl/apps/dh.c',
      'openssl/apps/dhparam.c',
      'openssl/apps/dsa.c',
      'openssl/apps/dsaparam.c',
      'openssl/apps/ec.c',
      'openssl/apps/ecparam.c',
      'openssl/apps/enc.c',
      'openssl/apps/engine.c',
      'openssl/apps/errstr.c',
      'openssl/apps/gendh.c',
      'openssl/apps/gendsa.c',
      'openssl/apps/genpkey.c',
      'openssl/apps/genrsa.c',
      'openssl/apps/nseq.c',
      'openssl/apps/ocsp.c',
      'openssl/apps/openssl.c',
      'openssl/apps/passwd.c',
      'openssl/apps/pkcs12.c',
      'openssl/apps/pkcs7.c',
      'openssl/apps/pkcs8.c',
      'openssl/apps/pkey.c',
      'openssl/apps/pkeyparam.c',
      'openssl/apps/pkeyutl.c',
      'openssl/apps/prime.c',
      'openssl/apps/rand.c',
      'openssl/apps/req.c',
      'openssl/apps/rsa.c',
      'openssl/apps/rsautl.c',
      'openssl/apps/s_cb.c',
      'openssl/apps/s_client.c',
      'openssl/apps/s_server.c',
      'openssl/apps/s_socket.c',
      'openssl/apps/s_time.c',
      'openssl/apps/sess_id.c',
      'openssl/apps/smime.c',
      'openssl/apps/speed.c',
      'openssl/apps/spkac.c',
      'openssl/apps/srp.c',
      'openssl/apps/ts.c',
      'openssl/apps/verify.c',
      'openssl/apps/version.c',
      'openssl/apps/x509.c',
    ],
    'openssl_defines_asm': [
      'AES_ASM',
      'CPUID_ASM',
      'OPENSSL_BN_ASM_MONT',
      'OPENSSL_CPUID_OBJ',
      'SHA1_ASM',
      'SHA256_ASM',
      'SHA512_ASM',
      'GHASH_ASM',
    ],
    'openssl_defines_non_arm': [
      'VPAES_ASM',
      'BN_ASM',
      'BF_ASM',
      'BNCO_ASM',
      'DES_ASM',
      'LIB_BN_ASM',
      'MD5_ASM',
      'OPENSSL_BN_ASM',
      'RIP_ASM',
      'RMD160_ASM',
      'WHIRLPOOL_ASM',
      'WP_ASM',
    ],
    'openssl_defines_x86_elf': [
      '<@(openssl_defines_non_arm)',
    ],
    'openssl_defines_x86_mac': [
      '<@(openssl_defines_non_arm)',
    ],
    'openssl_defines_x86_win': [
      '<@(openssl_defines_non_arm)',
    ],
    'openssl_defines_x64_elf': [
      '<@(openssl_defines_non_arm)',
      'OPENSSL_BN_ASM_MONT5',
      'OPENSSL_BN_ASM_GF2m',
      'OPENSSL_IA32_SSE2',
      'BSAES_ASM',
    ],
    'openssl_defines_x64_mac': [
      '<@(openssl_defines_non_arm)',
      'OPENSSL_BN_ASM_MONT5',
      'OPENSSL_BN_ASM_GF2m',
      'OPENSSL_IA32_SSE2',
      'BSAES_ASM',
    ],
    'openssl_defines_x64_win': [
      '<@(openssl_defines_non_arm)',
      'OPENSSL_BN_ASM_MONT5',
      'OPENSSL_BN_ASM_GF2m',
      'OPENSSL_IA32_SSE2',
      'BSAES_ASM',
    ],
    'openssl_include_dirs': [
      '.',
      'openssl',
      'openssl/crypto',
      'openssl/crypto/asn1',
      'openssl/crypto/evp',
      'openssl/crypto/md2',
      'openssl/crypto/modes',
      'openssl/crypto/store',
      'openssl/include',
    ],
#### Variables for openssl-cli  ####
    'openssl_cli_libraries_solaris': [
      '-lsocket',
      '-lnsl',
    ],
    'openssl_cli_libraries_win': [
      '-lws2_32.lib',
      '-lgdi32.lib',
      '-ladvapi32.lib',
      '-lcrypt32.lib',
      '-luser32.lib',
    ],
#### Variables for Target Defaults  ####
    'openssl_default_include_dirs': [
      '.',
      'openssl',
      'openssl/crypto',
      'openssl/crypto/asn1',
      'openssl/crypto/evp',
      'openssl/crypto/md2',
      'openssl/crypto/modes',
      'openssl/crypto/store',
      'openssl/include',
    ],
    'openssl_default_defines_all': [
      # No clue what these are for.
      'L_ENDIAN',
      'PURIFY',
      '_REENTRANT',

      # SSLv2 is known broken and has been superseded by SSLv3 for almost
      # twenty years now.
      'OPENSSL_NO_SSL2',

      # SSLv3 is susceptible to downgrade attacks (POODLE.)
      'OPENSSL_NO_SSL3',

      # Heartbeat is a TLS extension, that couldn't be turned off or
      # asked to be not advertised. Unfortunately this is unacceptable for
      # Microsoft's IIS, which seems to be ignoring whole ClientHello after
      # seeing this extension.
      'OPENSSL_NO_HEARTBEATS',
    ],
    'openssl_default_defines_win': [
      'MK1MF_BUILD',
      'WIN32_LEAN_AND_MEAN',
      'OPENSSL_SYSNAME_WIN32',
      'DSO_WIN32',
    ],
    'openssl_default_libraries_win': [
      '-lgdi32.lib',
      '-luser32.lib',
    ],
    'openssl_default_defines_not_win': [
      # ENGINESDIR must be defined if OPENSSLDIR is.
      'ENGINESDIR="/dev/null"',
      'TERMIOS',
      'DSO_DLFCN',
      'HAVE_DLFCN_H',
    ],
    'openssl_default_defines_mac': [
      # Set to ubuntu default path for convenience. If necessary,
      # override this at runtime with the SSL_CERT_DIR environment
      # variable.
      'OPENSSLDIR="/System/Library/OpenSSL/"',
    ],
    'openssl_default_defines_linux_others': [
      # Set to ubuntu default path for convenience. If necessary,
      # override this at runtime with the SSL_CERT_DIR environment
      # variable.
      'OPENSSLDIR="/etc/ssl"',
    ]
  }
}
