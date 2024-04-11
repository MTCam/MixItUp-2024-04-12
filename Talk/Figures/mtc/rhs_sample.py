def euler_operator(discr, eos, boundaries, cv, time=0.0):
    inviscid_flux_vol = inviscid_flux(discr, eos, cv)
    inviscid_flux_bnd = (
        inviscid_facial_flux(discr, eos=eos, cv_tpair=interior_trace_pair(discr, cv))
        + sum(inviscid_facial_flux(discr, eos=eos,
                                   cv_tpair=cross_rank_trace_pairs(discr, cv)))
        + sum(boundaries[btag].inviscid_boundary_flux(discr, btag=btag, cv=cv,
                                                      eos=eos, time=time)
              for btag in boundaries)
    )
    q_rhs = discr.inverse_mass(weak_local_div(discr, inviscid_flux_vol)
                               - discr.face_mass(inviscid_flux_bnd))
    return make_conserved(discr.dim, q=q_rhs)
